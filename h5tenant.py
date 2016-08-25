from dir import list_dir
from file import read_file, write_file
from option import get_opt
from output import print_replace, print_gather_dir_info
from replace import replace_tenant


def main(target_dir, tenant):
    print_gather_dir_info(target_dir)
    for path in list_dir(target_dir, '.js'):
        original_content = read_file(path)
        replaced_content, number_of_replace = replace_tenant(original_content, tenant)

        if number_of_replace > 0:
            print_replace(path, number_of_replace)
            write_file(path, replaced_content)


if __name__ == "__main__":
    directory, tenant = get_opt()
    main(directory, tenant)
