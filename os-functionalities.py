import os
import json
import shutil
import zipfile
import fnmatch

def copy_file(src, dest):
    shutil.copy(src, dest)

def move_file(src, dest):
    shutil.move(src, dest)

def create_directory(directory_path):
    os.makedirs(directory_path, exist_ok=True)

def get_directory_path(filename):
    return os.path.dirname(os.path.abspath(filename))

def write_to_file(filename, data, is_json=False):
    with open(filename, 'w') as f:
        if is_json:
            json.dump(data, f)
        else:
            f.write(data)

def read_from_file(filename, is_json=False):
    with open(filename, 'r') as f:
        if is_json:
            return json.load(f)
        else:
            return f.read()

def get_os_stats():
    import psutil
    return {
        "cpu_usage": psutil.cpu_percent(),
        "memory_usage": psutil.virtual_memory().percent,
        "storage_usage": psutil.disk_usage('/').percent
    }

def zip_files(files, output_filename):
    with zipfile.ZipFile(output_filename, 'w') as zf:
        for file in files:
            zf.write(file)

def zip_directory(directory_path, output_filename):
    shutil.make_archive(output_filename, 'zip', directory_path)

def unzip_file(zip_filename, output_directory):
    with zipfile.ZipFile(zip_filename, 'r') as zf:
        zf.extractall(output_directory)

def create_new_file(filename):
    open(filename, 'a').close()

def file_exists(file_path):
    return os.path.exists(file_path)

def directory_exists(directory_path):
    return os.path.isdir(directory_path)

def is_valid_path(path):
    return os.path.exists(path)

def get_directory_size(directory_path):
    total = 0
    for dirpath, dirnames, filenames in os.walk(directory_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            total += os.path.getsize(fp)
    return total

def get_file_size(file_path):
    return os.path.getsize(file_path)

def count_files_in_directory(directory_path, file_type='*'):
    count = 0
    for root, dirs, files in os.walk(directory_path):
        for name in fnmatch.filter(files, f"*.{file_type}"):
            count += 1
    return count

def search_file_in_directory(directory_path, file_name):
    for root, dirs, files in os.walk(directory_path):
        if file_name in files:
            return os.path.join(root, file_name)
    return None

def search_directory_in_path(path, directory_name):
    for root, dirs, files in os.walk(path):
        if directory_name in dirs:
            return os.path.join(root, directory_name)
    return None

# You can then use these functions to perform the actions as required.
