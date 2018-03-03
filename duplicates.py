import sys
import os
import collections


def get_size(file_path):
    return os.path.getsize(file_path)


def get_files_locations(directory):
    all_files_locations = collections.defaultdict(list)
    for dir_path, dir_names, files_names in os.walk(directory):
        for file_name in files_names:
            file_path = os.path.join(dir_path, file_name)
            file_size = get_size(file_path)
            all_files_locations[(file_name, file_size)].append(file_path)
    return all_files_locations


def get_duplicate_files(directory):
    duplicates = {}
    one_unique_file = 1
    files_locations = get_files_locations(directory)
    for (file_name, file_size), paths in files_locations.items():
        if len(paths) > one_unique_file:
            duplicates[(file_name, file_size)] = paths
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
        print('\n'.join(paths))
        print(delimiter)


if __name__ == '__main__':
    search_directory = sys.argv[1]
    if not os.path.isdir(search_directory):
        sys.exit('Directory path not available')
    duplicate_files = get_duplicate_files(search_directory)
    if not duplicate_files:
        sys.exit('No files duplicates')
    print_duplicates(duplicate_files)
