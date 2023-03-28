# coding=utf-8
"""
add coding=utf-8 into each py file in dir and its sub-dir
support python3+
"""

import os

from common import check_dir_exists


def add_encoding(dir_path):
    """ add coding=utf-8 into each py file in dir and its sub-dir """
    if not check_dir_exists(dir_path):
        return False

    for root_path, sub_dirs, sub_files in os.walk(dir_path):
        if len(sub_files) > 0:
            for sub_file in sub_files:
                # only python file (.py) to deal with
                if sub_file.endswith('.py'):
                    sub_file_path = os.path.join(root_path, sub_file)

                    # read content
                    with open(sub_file_path, 'r', encoding='UTF-8') as file:
                        file_content = file.read()

                    # skip files already contains coding setting
                    if file_content.startswith('# coding='):
                        continue

                    # add coding
                    file_content = '# coding=utf-8\n' + file_content

                    # write content
                    with open(sub_file_path, 'w', encoding='UTF-8') as file:
                        file.write(file_content)

                    print(f'add encoding into file {sub_file_path} successfully.')

        if len(sub_dirs) > 0:
            for sub_dir in sub_dirs:
                if sub_dir in ('__pycache__', '.git'):
                    continue
                sub_dir_path = os.path.join(root_path, sub_dir)
                add_encoding(sub_dir_path)


# ===== 主函数 =====
if __name__ == '__main__':
    v_dir_path = '..'
    add_encoding(v_dir_path)
