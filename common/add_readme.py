# coding=utf-8
""" 
description: add README.md in each project
python-version: 3+
"""

import os

from common import check_dir_exists


def add_readme(dir_path):
    """ add README.md file into the project dir """
    if not check_dir_exists(dir_path):
        return False

    # check README.md exists
    readme_path = os.path.join(dir_path, 'README.md')
    if os.path.exists(readme_path):
        print(f'the README.md is exist, skip creating: {readme_path}.')
        return True

    # create README.md file
    project_name = os.path.basename(dir_path)
    with open(readme_path, 'w', encoding='utf-8') as readme:
        readme.write(f'### {project_name}')

    print(f'create README.md successfully: {readme_path}.')
    return True


if __name__ == '__main__':
    v_dir_path = ''
    add_readme(v_dir_path)
