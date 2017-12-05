#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include "tsk/libtsk.h"
#include "tsk/fs/tsk_fs_i.h"
#include "tsk/fs/tsk_fs.h"
#include "tsk/base/tsk_base.h"
#include <sstream>

#pragma comment(lib, "Shell32.lib")

static uint8_t proc_dir(TSK_FS_INFO * fs_info,
	TSK_INUM_T dir_inum, const char *path)
{
	TSK_FS_DIR *fs_dir;
	size_t i;
	TSK_FS_FILE *fs_file;
	const char *MFTname = "$MFT";

	// open the directory
	if ((fs_dir = tsk_fs_dir_open_meta(fs_info, dir_inum)) == NULL) {
		fprintf(stderr, "Error opening directory: %" PRIuINUM "\n",
			dir_inum);
		tsk_error_print(stderr);
		return 1;
	}

	//find the $MFT position
	int MFTpos = 0;
	for (i = 0; i < tsk_fs_dir_getsize(fs_dir); i++)
	{
		if (strcmp(fs_dir->names[i].name, MFTname) == 0)
		{
			MFTpos = i;
			break;
		}
	}

	// get the entry
	if ((fs_file = tsk_fs_dir_get(fs_dir, MFTpos)) == NULL) {
		fprintf(stderr,
			"Error getting directory entry %" PRIuSIZE
			" in directory %" PRIuINUM "\n", i, dir_inum);
		tsk_error_print(stderr);
		return 1;
	}

	const TSK_FS_ATTR * fs_attr = tsk_fs_attrlist_get(fs_file->meta->attr, TSK_FS_ATTR_TYPE_NTFS_DATA);
	if (!fs_attr) {
		tsk_fs_file_close(fs_file);
		return 1;
	}

	fprintf(stdout, "%lld %lld\n", fs_attr->nrd.run->addr, fs_attr->size);
	return 0;
}


static uint8_t proc_fs(TSK_IMG_INFO * img_info, TSK_OFF_T start)
{
	TSK_FS_INFO *fs_info;

	// Try it as a file system
	if ((fs_info =
		tsk_fs_open_img(img_info, start, TSK_FS_TYPE_NTFS)) == NULL)
	{
		fprintf(stderr,
			"Error opening file system in partition at offset %" PRIuOFF
			"\n", start);
		tsk_error_print(stderr);
		return 1;
	}

	// Process the directories
	if (proc_dir(fs_info, fs_info->root_inum, "")) {
		fprintf(stderr,
			"Error processing file system in partition at offset %" PRIuOFF
			"\n", start);
		tsk_fs_close(fs_info);
		return 1;
	}

	tsk_fs_close(fs_info);
	return 0;
}

static uint8_t proc_vs(TSK_IMG_INFO * img_info, TSK_OFF_T start)
{
	TSK_VS_INFO *vs_info;
	// Open the volume system
	if ((vs_info =
		tsk_vs_open(img_info, start, TSK_VS_TYPE_DETECT)) == NULL) {
		if (tsk_verbose)
			fprintf(stderr,
				"Error determining volume system -- trying file systems\n");

		// There was no volume system, but there could be a file system
		tsk_error_reset();
		TskError::reset();
		if (proc_fs(img_info, start)) {
			return 1;
		}
	}
	else {
		fprintf(stderr, "Volume system open, examining each\n");

		// cycle through the partitions
		for (TSK_PNUM_T i = 0; i < vs_info->part_count; i++) {
			const TSK_VS_PART_INFO *vs_part;

			if ((vs_part = tsk_vs_part_get(vs_info, i)) == NULL) {
				fprintf(stderr, "Error getting volume %" PRIuPNUM "\n", i);
				continue;
			}

			// ignore the metadata partitions
			if (vs_part->flags & TSK_VS_PART_FLAG_META)
				continue;
			else {
				if (proc_fs(img_info,
					vs_part->start * vs_info->block_size)) {
					tsk_error_reset();
				}
			}
		}
		tsk_vs_close(vs_info);
	}
	return 0;
}

int main(int argc, char **argv1)
{
	TSK_IMG_INFO *img_info;
	TSK_TCHAR **argv;
	std::wstring volPath = L"\\\\.\\";

#ifdef TSK_WIN32
	// On Windows, get the wide arguments (mingw doesn't support wmain)
	argv = CommandLineToArgvW(GetCommandLineW(), &argc);
	if (argv == NULL) {
		fprintf(stderr, "Error getting wide arguments\n");
		exit(1);
	}
#else
	argv = (TSK_TCHAR **)argv1;
#endif

	if (argc != 2) {
		fprintf(stderr, "Missing volumn name\n");
		exit(1);
	}

	// to generate real volumn path
	volPath += std::wstring(argv[1]);
	std::wstringstream wss;
	wss << volPath.c_str();
	std::wstring ws = wss.str();
	const TSK_TCHAR* realPath = ws.c_str();

	// open the disk image
	img_info = tsk_img_open_sing(realPath, TSK_IMG_TYPE_DETECT, 0);
	if (img_info == NULL) {
		fprintf(stderr, "Error opening file\n");
		tsk_error_print(stderr);
		exit(1);
	}

	// process the volume starting at sector 0
	if (proc_vs(img_info, 0)) {
		tsk_error_print(stderr);
		tsk_img_close(img_info);
		exit(1);
	}

	// close the image
	tsk_img_close(img_info);
	return 0;
}
