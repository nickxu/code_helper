# coding=utf-8
""" 
description: clear temporary files or directories
python-version: 3+
"""

import os
import shutil

from common import check_dir_exists


def clear_temp_files(dir_path):
    """  clear temporary files or directories """
    if not check_dir_exists(dir_path):
        return False

    # temporary file names
    temp_file_names = ('vendor', 'node_modules')
    for temp_file_name in temp_file_names:
        temp_file_path = os.path.join(dir_path, temp_file_name)
        if os.path.exists(temp_file_path):
            # clear directory and remove it
            if os.path.isdir(temp_file_path):
                shutil.rmtree(temp_file_path)
            # remove file
            elif os.path.isfile(temp_file_path):
                os.remove(temp_file_path)

    pass


if __name__ == '__main__':
    v_dir_path = 'D:/workspaces/php-workspace/sample'
    clear_temp_files(v_dir_path)
