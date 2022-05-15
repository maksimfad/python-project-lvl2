#!/usr/bin/env python
import json
import yaml


def parcing_func(file_path1, file_path2):
    if '.json' in file_path1:
        first_file = json.load(open(file_path1))
    elif '.yml' or '.yaml' in file_path1:
        first_file = yaml.load(open(file_path1), Loader=yaml.SafeLoader)
    if '.json' in file_path2:
        second_file = json.load(open(file_path2))
    elif '.yml' or '.yaml' in file_path1:
        second_file = yaml.load(open(file_path2), Loader=yaml.SafeLoader)
    return first_file, second_file
