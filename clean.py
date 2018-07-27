"""
Logic:

1. Get list of folders in directory, including current directory
2. For each folder:
    1.  Open folder
    2.  Delete every file in the folder ending in ['.aux', '.fdb_latexmk', '.fls', '.log', '.synctex.gz', '.dvi']
"""

import os

directories = ['.','./archive/_tex_output']
with os.scandir(path='.') as it:
    for entry in it:
        if not entry.name.startswith('.') and entry.is_dir():
            directories.append(entry.name)

deleted_files = []
for directory in directories:
    files_to_delete = []
    with os.scandir(path=directory) as it:
        for entry in it:
            if not entry.name.startswith('.') and (
                entry.name.endswith('.aux') or
                entry.name.endswith('.fdb_latexmk') or
                entry.name.endswith('.fls') or
                entry.name.endswith('.log') or
                entry.name.endswith('.synctex.gz') or
                entry.name.endswith('.dvi') or
                entry.name.endswith('.out') or
                entry.name.endswith('.toc')):
                files_to_delete.append(entry.name)
    for file in files_to_delete:
        del_string = directory + '/' + file
        deleted_files.append(del_string)
        os.remove(del_string)

print('Deleted files:')
for file in deleted_files:
    print(file)