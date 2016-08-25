from output import print_read_file_error


def read_file(path):
    try:
        with open(path, 'r', encoding="utf8") as f:
            content = f.read()
        f.close()
        return content
    except Exception as e:
        print_read_file_error(path,e)
        return ''


def write_file(path, content):
    with open(path, 'w', encoding="utf8") as f:
        f.write(content)
    f.close()
