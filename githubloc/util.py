import configparser
import os
from shutil import copyfile


def file_is_empty(path):
    return os.stat(path).st_size == 0


def parse_config(config_file):

    if not os.path.isfile(config_file):
        print(bcolors.WARNING + config_file + ' not found, please create one.' + bcolors.ENDC)
        raise SystemExit

    conf = configparser.ConfigParser()
    conf.read(config_file)

    return conf['default']


def check_if_not_create(file, template):
    if not os.path.isfile(file):
        os.makedirs(os.path.dirname(file), exist_ok=True)
        copyfile(template, file)


def replace_last(s, old, new):
    return s[::-1].replace(old[::-1], new[::-1], 1)[::-1]


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
