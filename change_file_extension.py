# coding=utf-8
""" 
description: change file extension
python-version: 3+
"""
import os
import re
import shutil


def change_file_extension(source_file_path, new_extension):
    """ change file extension """
    if not os.path.exists(source_file_path) or not os.path.isfile(source_file_path):
        print(f'the source file path is not exist. {source_file_path}')
        return False

    new_file_path = re.compile('^(.*)\w+').sub(f'\\1.{new_extension}', source_file_path)
    if os.path.exists(new_file_path):
        print(f'the target file path of new extension is already exist. {new_file_path}')
        return False

    # rename file
    shutil.move(source_file_path, new_file_path)
    return os.path.exists(new_file_path)


if __name__ == '__main__':
    v_file_path = ''
    v_extension = ''
    change_file_extension(v_file_path, v_extension)
