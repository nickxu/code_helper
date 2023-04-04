# coding=utf-8
""" 
description: 
python-version: 3+
"""
import os

from common import check_dir_exists


def process_dir_recursively(dir_path, func_name, only_sons = False, file_filter_func=None, dir_filter_func=None, func_params: set = ()):
    """ process directories recursively """
    if not check_dir_exists(dir_path):
        return False

    # iterate sub files and directories
    for root, dirs, files in os.walk(dir_path):
        # only_sons: True: just process next level
        if not only_sons:
            # get into sub directory to process its sub files
            for sub_dir in dirs:
                sub_dir_path = os.path.join(root, sub_dir)
                if dir_filter_func and not dir_filter_func(sub_dir_path):
                    continue

                if len(func_params) > 0:
                    process_dir_recursively(sub_dir_path, func_name, file_filter_func, dir_filter_func, *func_params)
                else:
                    process_dir_recursively(sub_dir_path, func_name, file_filter_func, dir_filter_func)

        # process sub files
        for sub_file in files:
            sub_file_path = os.path.join(root, sub_file)
            if file_filter_func and not file_filter_func(sub_file_path):
                continue

            if len(func_params) > 0:
                func_name(sub_file_path, *func_params)
            else:
                func_name(sub_file_path)
