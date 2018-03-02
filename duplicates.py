import sys
import os


def get_size(dir_path, files_names):
    files_sizes = []
    for file_name in files_names:
        file_path = os.path.join(dir_path, file_name)
        files_sizes.append(os.path.getsize(file_path))
    return files_sizes


def get_all_files(directory):
    all_files = {}
    for dir_path, dir_names, files_names in os.walk(directory):
        if not files_names:
            continue
        files_sizes = get_size(dir_path, files_names)
        id_files = zip(files_names, files_sizes)
        for id_file in id_files:
            if id_file not in all_files:
                all_files[id_file] = []
            all_files[id_file].append(os.path.abspath(dir_path))
    return all_files


def get_duplicate_files(directory):
    duplicates = {}
    one_unique_file = 1
    all_files = get_all_files(directory)
    for id_file, paths in all_files.items():
        if len(paths) > one_unique_file:
            duplicates[id_file] = paths
    return duplicates


def print_duplicates(duplicate):
    print('Duplicates:')
    for id_file, paths in duplicate.items():
        file_name = id_file[0]
        file_size = id_file[1]
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
    # search_directory = '/home/dany/devman/11_duplicates'
    if not os.path.isdir(search_directory):
        sys.exit('Directory path not available')
    duplicate_files = get_duplicate_files(search_directory)
    if not duplicate_files:
        sys.exit('No files duplicates')
    print_duplicates(duplicate_files)
