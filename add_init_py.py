# coding=utf-8
""" 
description: add __init__.py into every python package dir
python-version: 3+
"""

import os

from common import check_dir_exists


def add_init_py(dir_path):
    """ add init.py file into every python package dir """

    if not check_dir_exists(dir_path):
        return False

    # iterate sub directories
    for sub_dir in os.listdir(dir_path):
        sub_dir_path = os.path.join(dir_path, sub_dir)

        # skip non-directory file
        if not os.path.isdir(sub_dir_path):
            continue

        # check init.py exists
        init_py_path = os.path.join(sub_dir_path, '__init__.py')
        if os.path.exists(init_py_path):
            print(f'the __init__.py is exist, skip creating: {init_py_path}.')
            return True

        # create init.py file
        with open(init_py_path, 'w', encoding='utf-8') as init_py:
            init_py.write('# coding=utf-8')

        print(f'create __init__.py successfully: {init_py_path}.')
    return True


if __name__ == '__main__':
    v_dir_path = '.'
    add_init_py(v_dir_path)
