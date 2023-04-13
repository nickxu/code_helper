# coding=utf-8
""" 
description: statistic code files
python-version: 3+
"""
import os
import re

from common import check_dir_exists


def statistic_code_files(dir_path, file_extensions: list = None):
    """ statistic code files """
    result_files = set()

    if not check_dir_exists(dir_path):
        return result_files

    # iterate sub files and directories
    file_extension_pattern = re.compile(r'^.+[.](\w+)$')
    for root, dirs, files in os.walk(dir_path):
        # process sub files
        for sub_file in files:
            sub_file_path = os.path.join(root, sub_file)
            file_extension = file_extension_pattern.sub('\\1', sub_file)
            if file_extensions and len(file_extensions) > 0:
                if file_extension in file_extensions:
                    result_files.add(sub_file_path)
            else:
                result_files.add(sub_file_path)

    return result_files


if __name__ == '__main__':
    v_dir_path = ''
    statistic_code_files(v_dir_path)
