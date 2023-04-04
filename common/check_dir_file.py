# coding=utf-8
""" 
description: 
python-version: 3+
"""
import os


def check_dir_exists(dir_path):
    """  """
    if not os.path.exists(dir_path):
        print(f'the directory of given path is not exist: {dir_path}')
        return False

    if not os.path.isdir(dir_path):
        print(f'the directory of given path is not a directory: {dir_path}')
        return False

    return True


def check_file_exists(file_path):
    """  """
    if not os.path.exists(file_path):
        print(f'the file of given path is not exist: {file_path}')
        return False

    if not os.path.isfile(file_path):
        print(f'the directory of given path is not a file: {file_path}')
        return False

    return True
