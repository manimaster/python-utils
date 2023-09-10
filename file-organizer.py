"""
File Organizer

This script organizes files in a directory into respective folders based on their extensions.
"""

import os
from shutil import move

def organize_files(directory):
    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)):
            file_ext = filename.split('.')[-1]
            ext_folder = os.path.join(directory, file_ext)
            if not os.path.exists(ext_folder):
                os.makedirs(ext_folder)
            move(os.path.join(directory, filename), os.path.join(ext_folder, filename))

directory = input("Enter directory path to organize: ")
organize_files(directory)
