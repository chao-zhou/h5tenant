import os
from getopt import GetoptError, getopt

import sys


def get_opt():
    if len(sys.argv) == 1:
        show_help()
        sys.exit()
    return parse_opt(sys.argv[1:])


def parse_opt(argv):
    try:
        opts, args = getopt(argv, 'hd:t:', ['help', 'directory=', 'tenant='])
    except GetoptError:
        show_help()
        sys.exit()

    return get_opt_val(opts)


def get_opt_val(opts):
    tenant = 'dev'
    directory = os.getcwd()
    for opt, arg in opts:
        if opt in ('-h', '--help'):
            show_help()
            sys.exit()
        elif opt in ('-d', '--directory'):
            directory = arg
        elif opt in ('-t', '--tenant'):
            tenant = arg
    return directory, tenant


def show_help():
    print('h5tenant.py -d <directory> -t <tenant>')
    print('h5tenant.py --directory=<directory> --tenant=<tenant>')
