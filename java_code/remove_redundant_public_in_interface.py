# coding=utf-8
""" 
description:  remove redundant public in interface
python-version: 3+
"""

import os
import re

from common import process_dir_recursively, check_file_exists


def remove_redundant_public_in_interface(file_path):
    """ remove redundant public in interface """
    if not check_file_exists(file_path):
        return False

    public_method_pattern = re.compile(r'^([\t ]+)public[\t ]+(\w+.+\(.*\).*)$')

    new_lines = []
    for line in open(file_path, 'r', encoding='utf-8'):
        strip_line = line.strip()
        # keep empty line
        if len(strip_line) == 0:
            new_lines.append('\n')
            continue

        # remove public
        if public_method_pattern.match(strip_line):
            new_line = public_method_pattern.sub('\\1\\2', strip_line)
            new_lines.append(new_line)
        else:
            # keep other
            new_lines.append(strip_line)

    # write content back
    with open(file_path, 'w', encoding='utf-8') as file:
        for line in new_lines:
            file.write(line + '\n')

    return True


def only_java_file(file_path: str):
    return file_path.endswith('.java')


def except_git_logs(dir_path):
    return os.path.basename(dir_path) not in ('.git', 'logs')


if __name__ == '__main__':
    v_dir_path = ''
    process_dir_recursively(v_dir_path, remove_redundant_public_in_interface,
                            file_filter_func=only_java_file,
                            dir_filter_func=except_git_logs)
