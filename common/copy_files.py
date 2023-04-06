# coding=utf-8
""" 
description: copy files from source directory to target directory recursively
python-version: 3+
"""

import shutil
from common import check_dir_exists

def copy_files_under_dir(source_dir, target_dir):
    """ copy files from source directory to target directory recursively """
    if not check_dir_exists(source_dir):
        return False

    shutil.copytree(source_dir, target_dir)
    return True

if __name__ == '__main__':
    v_source_dir_path = ''
    v_target_dir_path = ''
    copy_files_under_dir(v_source_dir_path, v_target_dir_path)
