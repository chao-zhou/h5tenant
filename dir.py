import os


def list_dir(path, ext=''):
    if os.path.isfile(path) and is_extension(path, ext):
        return [path]

    if os.path.isfile(path):
        return []

    path_list = []
    for f in os.listdir(path):
        f_path = os.path.join(path, f)
        if os.path.isfile(f_path) and is_extension(f_path, ext):
            path_list.append(f_path)
            continue
        elif os.path.isdir(f_path):
            sub_path_list = list_dir(f_path, ext)
            path_list += sub_path_list
    return path_list


def is_extension(path, ext):
    if ext == '':
        return 1

    if ext[0] != '.':
        ext = '.' + ext
    name, extension = os.path.splitext(path)
    return extension == ext
