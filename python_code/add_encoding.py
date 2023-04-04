# coding=utf-8
"""
add coding=utf-8 into each py file in dir and its sub-dir
support python3+
"""

import os

from common import process_dir_recursively, check_file_exists


def add_encoding(sub_file_path):
    """ add coding=utf-8 into each py file in dir and its sub-dir """
    if not check_file_exists(sub_file_path):
        return False

    # read content
    with open(sub_file_path, 'r', encoding='UTF-8') as file:
        file_content = file.read()

    # skip files already contains coding setting
    if file_content.startswith('# coding='):
        return False

    # add coding
    file_content = '# coding=utf-8\n' + file_content

    # write content
    with open(sub_file_path, 'w', encoding='UTF-8') as file:
        file.write(file_content)

    print(f'add encoding into file {sub_file_path} successfully.')
    return True


def only_python_files(file_path):
    return file_path.endswith('.py')


def not_cache_and_git(dir_path):
    dir_name = os.path.join(dir_path)
    return dir_name not in ('__pycache__', '.git')


# ===== 主函数 =====
if __name__ == '__main__':
    v_dir_path = '..'
    process_dir_recursively(v_dir_path, add_encoding, file_filter_func=only_python_files, dir_filter_func=not_cache_and_git)
