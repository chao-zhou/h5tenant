debug_info_template = '[Info] File:{0} Replace:{1}'
read_file_error_template = '[Error] Message:{0} File:{1}'
gather_dir_info_template = '[Verbose] Gathering Directory Info. Path: {0}'


def print_replace(path, number_of_replace):
    print(debug_info_template.format(path, number_of_replace))


def print_read_file_error(path, error):
    print(read_file_error_template.format(error, path))


def print_gather_dir_info(path):
    print(gather_dir_info_template.format(path))
