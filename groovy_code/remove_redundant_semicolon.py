# coding=utf-8
""" 
description: remove redundant semicolon in groovy files
python-version: 3+
"""

import re

from common import check_file_exists, process_dir_recursively


def remove_redundant_semicolon(sub_file_path):
    """ remove redundant semicolon in groovy files """
    semicolon_end_regex = re.compile('[\t ]*;[\t ]*$')
    if not check_file_exists(sub_file_path):
        return False

    # read every line and remove the semicolon end
    new_lines = []
    for line in open(sub_file_path, 'r', encoding='utf-8'):
        # WARN: keep the left blanks
        new_line = semicolon_end_regex.sub('', line.rstrip())
        new_lines.append(new_line)

    with open(sub_file_path, 'w', encoding='utf-8') as file:
        for line in new_lines:
            file.write(line + '\n')


def only_groovy_files(file_path):
    return file_path.endswith('.groovy')


if __name__ == '__main__':
    v_dir_path = 'D:/workspaces/groovy_demo'
    process_dir_recursively(v_dir_path, remove_redundant_semicolon, file_filter_func=only_groovy_files)
