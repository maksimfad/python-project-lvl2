#!/usr/bin/env python
import json
import yaml
import argparse

from format.formatter import stylish


def parcing_arguments():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format',
                        default=stylish, help='set format of output')
    args = parser.parse_args()
    return args


def parcing_files(file_path1, file_path2):
    file_paths = (file_path1, file_path2)
    files = []
    for file_path in file_paths:
        if '.json' in file_path:
            file = json.load(open(file_path))
        elif '.yml' or '.yaml' in file_path:
            file = yaml.load(open(file_path), Loader=yaml.SafeLoader)
        files.append(file)
    return files
