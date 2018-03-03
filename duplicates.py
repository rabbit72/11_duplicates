import sys
import os
import collections


def get_id_files(dir_path, files_names):
    files_sizes = []
    for file_name in files_names:
        file_path = os.path.join(dir_path, file_name)
        files_sizes.append(os.path.getsize(file_path))
    id_files = zip(files_names, files_sizes)
    return id_files


def get_all_id_files(directory):
    all_id_files = collections.defaultdict(list)
    for dir_path, dir_names, files_names in os.walk(directory):
        id_files = get_id_files(dir_path, files_names)
        for id_file in id_files:
            all_id_files[id_file].append(os.path.abspath(dir_path))
    return all_id_files


def get_duplicate_files(directory):
    duplicates = {}
    one_unique_file = 1
    all_id_files = get_all_id_files(directory)
    for id_file, paths in all_id_files.items():
        if len(paths) > one_unique_file:
            duplicates[id_file] = paths
    return duplicates


def print_duplicates(duplicate):
    print('Duplicates:')
    for (file_name, file_size), paths in duplicate.items():
        delimiter = '-' * 50
        print(delimiter)
        print(
            'File: {0}\n'
            'Size: {1}\n'
            'Paths:'.format(file_name, file_size))
        for path in paths:
            print(path)
        print(delimiter)


if __name__ == '__main__':
    search_directory = sys.argv[1]
    if not os.path.isdir(search_directory):
        sys.exit('Directory path not available')
    duplicate_files = get_duplicate_files(search_directory)
    if not duplicate_files:
        sys.exit('No files duplicates')
    print_duplicates(duplicate_files)
