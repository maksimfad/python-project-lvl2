#!/usr/bin/env python
import json
import yaml


def parcing_func(file_path1, file_path2):
    file_paths = (file_path1, file_path2)
    files = []
    for file_path in file_paths:
        if '.json' in file_path:
            file = json.load(open(file_path))
        elif '.yml' or '.yaml' in file_path:
            file = yaml.load(open(file_path), Loader=yaml.SafeLoader)
        files.append(file)
    return files
