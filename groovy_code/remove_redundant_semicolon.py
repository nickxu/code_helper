# coding=utf-8
""" 
description: remove redundant semicolon in groovy files
python-version: 3+
"""

import os
import re

from common import check_dir_exists


def do_it(dir_path):
    """ remove redundant semicolon in groovy files """
    if not check_dir_exists(dir_path):
        return False

    semicolon_end_regex = re.compile('[\t ]*;[\t ]*$')
    for root, sub_dirs, sub_files in dir_path:
        for sub_dir in sub_dirs:
            sub_dir_path = os.path.join(root, sub_dir)
            do_it(sub_dir_path)

        for sub_file in sub_files:
            if not sub_file.endswith('.groovy'):
                continue

            # read every line and remove the semicolon end
            sub_file_path = os.path.join(root, sub_file)
            new_lines = []
            for line in open(sub_file_path, 'r', encoding='utf-8'):
                # WARN: keep the left blanks
                new_line = semicolon_end_regex.sub('', line.rstrip())
                new_lines.append(new_line)

            with open(sub_file_path, 'w', encoding='utf-8') as file:
                for line in new_lines:
                    file.write(line + '\n')


if __name__ == '__main__':
    v_dir_path = ''
    do_it(v_dir_path)
