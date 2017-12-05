{
   'targets':[
        {
            'target_name':'helloWW',
            'type':'executable',
            'dependencies':[],
            'defines':[],
            'include_dirs':['tsk','tsk/fs','tsk/base','tsk/img','.',],
            'sources':[
                'testSleuthkit.cpp',
				'tsk/auto/auto.cpp',
				'tsk/auto/auto_db.cpp',
				'tsk/auto/case_db.cpp',
				'tsk/auto/db_postgresql.cpp',
				'tsk/auto/db_sqlite.cpp',
				'tsk/auto/guid.cpp',
				'tsk/auto/sqlite3.c',
				'tsk/auto/tsk_db.cpp',
				'tsk/base/crc.c',
				'tsk/base/md5c.c',
				'tsk/base/mymalloc.c',
				'tsk/base/sha1c.c',
				'tsk/base/tsk_endian.c',
				'tsk/base/tsk_error.c',
				'tsk/base/tsk_error_win32.cpp',
				'tsk/base/tsk_list.c',
				'tsk/base/tsk_lock.c',
				'tsk/base/tsk_parse.c',
				'tsk/base/tsk_printf.c',
				'tsk/base/tsk_stack.c',
				'tsk/base/tsk_unicode.c',
				'tsk/base/tsk_version.c',
				'tsk/base/XGetopt.c',
				'tsk/fs/dcalc_lib.c',
				'tsk/fs/dcat_lib.c',
				'tsk/fs/dls_lib.c',
				'tsk/fs/dstat_lib.c',
				'tsk/fs/exfatfs.c',
				'tsk/fs/exfatfs_dent.c',
				'tsk/fs/exfatfs_meta.c',
				'tsk/fs/ext2fs.c',
				'tsk/fs/ext2fs_dent.c',
				'tsk/fs/ext2fs_journal.c',
				'tsk/fs/fatfs.c',
				'tsk/fs/fatfs_dent.cpp',
				'tsk/fs/fatfs_meta.c',
				'tsk/fs/fatfs_utils.c',
				'tsk/fs/fatxxfs.c',
				'tsk/fs/fatxxfs_dent.c',
				'tsk/fs/fatxxfs_meta.c',
				'tsk/fs/ffind_lib.c',
				'tsk/fs/ffs.c',
				'tsk/fs/ffs_dent.c',
				'tsk/fs/fls_lib.c',
				'tsk/fs/fs_attr.c',
				'tsk/fs/fs_attrlist.c',
				'tsk/fs/fs_block.c',
				'tsk/fs/fs_dir.c',
				'tsk/fs/fs_file.c',
				'tsk/fs/fs_inode.c',
				'tsk/fs/fs_io.c',
				'tsk/fs/fs_load.c',
				'tsk/fs/fs_name.c',
				'tsk/fs/fs_open.c',
				'tsk/fs/fs_parse.c',
				'tsk/fs/fs_types.c',
				'tsk/fs/hfs.c',
				'tsk/fs/hfs_dent.c',
				'tsk/fs/hfs_journal.c',
				'tsk/fs/hfs_unicompare.c',
				'tsk/fs/icat_lib.c',
				'tsk/fs/ifind_lib.c',
				'tsk/fs/ils_lib.c',
				'tsk/fs/iso9660.c',
				'tsk/fs/iso9660_dent.c',
				'tsk/fs/nofs_misc.c',
				'tsk/fs/ntfs.c',
				'tsk/fs/ntfs_dent.cpp',
				'tsk/fs/rawfs.c',
				'tsk/fs/swapfs.c',
				'tsk/fs/unix_misc.c',
				'tsk/fs/walk_cpp.cpp',
				'tsk/fs/yaffs.cpp',
				'tsk/hashdb/binsrch_index.cpp',
				'tsk/hashdb/encase.c',
				'tsk/hashdb/hashkeeper.c',
				'tsk/hashdb/hdb_base.c', 
				'tsk/hashdb/idxonly.c',
				'tsk/hashdb/md5sum.c',
				'tsk/hashdb/nsrl.c',
				'tsk/hashdb/sqlite_hdb.cpp',
				'tsk/hashdb/tsk_hashdb.c',
				'tsk/img/aff.c',
				'tsk/img/ewf.c',
				'tsk/img/img_io.c',
				'tsk/img/img_open.c',
				'tsk/img/img_types.c',
				'tsk/img/mult_files.c',
				'tsk/img/raw.c',
				'tsk/img/vhd.c',
				'tsk/img/vmdk.c',
				'tsk/vs/bsd.c',
				'tsk/vs/dos.c',
				'tsk/vs/gpt.c',
				'tsk/vs/mac.c',
				'tsk/vs/mm_io.c',
				'tsk/vs/mm_open.c',
				'tsk/vs/mm_part.c',
				'tsk/vs/mm_types.c',
				'tsk/vs/sun.c',
				'tsk/auto/db_connection_info.h',
				'tsk/auto/guid.h',
				'tsk/auto/sqlite3.h',
				'tsk/auto/tsk_auto.h',
				'tsk/auto/tsk_auto_i.h',
				'tsk/auto/tsk_case_db.h',
				'tsk/auto/tsk_db.h',
				'tsk/auto/tsk_db_postgresql.h',
				'tsk/auto/tsk_db_sqlite.h',
				'tsk/base/crc.h',
				'tsk/base/tsk_base.h',
				'tsk/base/tsk_base_i.h',
				'tsk/base/tsk_os.h',
				'tsk/fs/tsk_exfatfs.h',
				'tsk/fs/tsk_ext2fs.h',
				'tsk/fs/tsk_fatfs.h',
				'tsk/fs/tsk_fatxxfs.h',
				'tsk/fs/tsk_ffs.h',
				'tsk/fs/tsk_fs.h',
				'tsk/fs/tsk_fs_i.h',
				'tsk/fs/tsk_hfs.h',
				'tsk/fs/tsk_iso9660.h',
				'tsk/fs/tsk_ntfs.h',
				'tsk/fs/tsk_yaffs.h',
				'tsk/hashdb/tsk_hashdb.h',
				'tsk/hashdb/tsk_hashdb_i.h',
				'tsk/hashdb/tsk_hash_info.h',
				'tsk/img/aff.h',
				'tsk/img/ewf.h',
				'tsk/img/raw.h',
				'tsk/img/tsk_img.h',
				'tsk/img/tsk_img_i.h',
				'tsk/img/vhd.h',
				'tsk/img/vmdk.h',
				'tsk/libtsk.h',
				'tsk/tsk_tools_i.h',
				'tsk/vs/tsk_bsd.h',
				'tsk/vs/tsk_dos.h',
				'tsk/vs/tsk_gpt.h',
				'tsk/vs/tsk_mac.h',
				'tsk/vs/tsk_sun.h',
				'tsk/vs/tsk_vs.h',
				'tsk/vs/tsk_vs_i.h',
            ],
            'conditions':[]
        }
    ],  
}
