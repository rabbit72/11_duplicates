import sys
import os
import collections


def get_size(file_path):
    return os.path.getsize(file_path)


def get_files_locations(directory):
    files_locations = collections.defaultdict(list)
    for dir_path, dir_names, files_names in os.walk(directory):
        for file_name in files_names:
            file_path = os.path.join(dir_path, file_name)
            file_size = get_size(file_path)
            files_locations[(file_name, file_size)].append(file_path)
    return files_locations


def get_duplicate_files(files_locations):
    duplicates = {}
    one_unique_file = 1
    for (file_name, file_size), paths in files_locations.items():
        if len(paths) > one_unique_file:
            duplicates[(file_name, file_size)] = paths
    return duplicates


def print_duplicates(duplicates):
    delimiter = '-' * 50
    if not duplicates:
        print(delimiter)
        print('No files duplicates')
        print(delimiter)
    else:
        print('Duplicates:')
        for (file_name, file_size), paths in duplicates.items():
            print(delimiter)
            print(
                'File: {0}\n'
                'Size: {1}\n'
                'Paths:'.format(file_name, file_size))
            print('\n'.join(paths))
            print(delimiter)


if __name__ == '__main__':
    try:
        search_directory = sys.argv[1]
        if not os.path.isdir(search_directory):
            exit('Directory path not available')
        files_locations = get_files_locations(search_directory)
        duplicate_files = get_duplicate_files(files_locations)
        print_duplicates(duplicate_files)
    except IndexError:
        exit('No directory path. Try again entering the path')
