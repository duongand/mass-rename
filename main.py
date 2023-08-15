from os import listdir, scandir, stat, rename, path

staging_directory = r'staging_directory'
final_directory = r'final_directory'
file_prefix = "prefix"

def count_files(path):
    return len(listdir(path)) + 1

def get_file_infos(path):
    files_array = []
    files = scandir(path)

    for file in files:
        if file.is_file():
            files_array.append([file.name, stat(file.path).st_mtime])

    files.close()
    return sorted(files_array, key=lambda x: x[1])

def rename_files(staging_directory, files, current_count):
    for file in files:
        rename(src=path.join(staging_directory, file[0]), dst=path.join(staging_directory, file_prefix + "." + str(current_count) + ".jpg"))
        current_count += 1

def main():
    file_count = count_files(final_directory)
    sorted_array = get_file_infos(staging_directory)
    rename_files(staging_directory, sorted_array, file_count)

if __name__ == '__main__':
    main()