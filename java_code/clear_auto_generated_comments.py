# coding=utf-8
""" 
description: clear the "// TODO Auto-generated catch block" in java code
python-version: 3+
"""

import os

def clear_auto_generated_comments(dir_path):
    """ clear the "// TODO Auto-generated catch block" in java code """
    # check if the directory exists
    if not os.path.exists(dir_path):
        print(f'the directory path is not exist: {dir_path}.')
        return

    # iterate sub files and directories
    for root, dirs, files in os.walk(dir_path):

        # get into sub directory to process its sub files
        for sub_dir in dirs:
            sub_dir_path = os.path.join(root, sub_dir)
            clear_auto_generated_comments(sub_dir_path)

        # process sub files
        for sub_file in files:
            if not sub_file.endswith('.java'):
                continue

            sub_file_path = os.path.join(root, sub_file)
            # default encoding is utf-8
            with open(sub_file_path, 'r', encoding='UTF-8') as file:
                file_content = file.read()

            # only process the files which contains the comment.
            if '// TODO Auto-generated catch block' in file_content:
                file_content = file_content.replace('// TODO Auto-generated catch block', '')

                # write the processed content back to the file
                with open(sub_file_path, 'w', encoding='UTF-8') as file:
                    file.write(file_content)

                print(f'update the content of file : {sub_file_path}')


if __name__ == '__main__':
    v_dir_path = r'D:\workspaces\java_demo\src\main\java'
    clear_auto_generated_comments(v_dir_path)
