# A simple python script that converts files created by one file system to another
# Example file created on windows file systems 'folder1\folder2\file.txt' 
# would become 'folder1/folder2/file.txt' on unix file systems
# Usage: 
#   python fs_converter.py /Users/dragan/Code/FileSystemConverter \\

import os
import sys

from shutil import move

# Functional not operator
def _not(func):
    def not_func(*args, **kwargs):
        return not func(*args, **kwargs)
    return not_func

# Lists all files from root directory
def ListFiles(root):
    return [file 
    for file in os.listdir(root) 
    if os.path.isfile(os.path.join(root, file))]

# Checks whether a file is a folder or a file from the
# perspective of the old file system
# Note: not a perfect solution, but works for most unix and windows environments
def IsFile(file):
    return os.stat(file).st_size > 0

# Creates a directory tree in the current file system
# given list of folders and the delimiter of the old file system 
def MakeDirectoryTree(folders, delimiter):
    for folder in folders:
        subFolders = filter(None, folder.split(delimiter))
        topFolder = "";
        for subFolder in subFolders:
            topFolder = os.path.join(topFolder, subFolder)
            if not os.path.exists(topFolder):
                os.mkdir(topFolder)
        os.remove(folder)

# Moves files from the old file system format, to the current one
def MoveFiles(files, delimiter):
    for file in files:
        move(file, file.replace(delimiter, os.path.sep))

if __name__ == '__main__':
    delimiter = sys.argv[2]
    allFiles = ListFiles(sys.argv[1])
    MakeDirectoryTree(filter(_not(IsFile), allFiles), delimiter)
    MoveFiles(filter(IsFile, allFiles), delimiter)