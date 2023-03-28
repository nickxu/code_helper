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
