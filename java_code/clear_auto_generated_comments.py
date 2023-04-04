# coding=utf-8
""" 
description: clear the "// TODO Auto-generated catch block" in java code
python-version: 3+
"""

from common import process_dir_recursively


def clear_auto_generated_comments(file_path):
    """ clear the "// TODO Auto-generated catch block" in java code """

    # default encoding is utf-8
    with open(file_path, 'r', encoding='UTF-8') as file:
        file_content = file.read()

    # only process the files which contains the comment.
    if '// TODO Auto-generated catch block' in file_content:
        file_content = file_content.replace('// TODO Auto-generated catch block', '')

        # write the processed content back to the file
        with open(file_path, 'w', encoding='UTF-8') as file:
            file.write(file_content)

        print(f'update the content of file : {file_path}')


def only_java_files(file_path):
    return file_path.endswith('.java')


if __name__ == '__main__':
    v_dir_path = r'D:\workspaces\java_demo\src\main\java'
    process_dir_recursively(v_dir_path, clear_auto_generated_comments, file_filter_func=only_java_files)
