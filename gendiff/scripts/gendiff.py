#!/usr/bin/env python

import argparse
import json
# from unittest import result


def main():
    # print("Hello!")
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()

    # print(str(args.first_file))
    # print(args.second_file)
    diff = generate_diff(args.first_file, args.second_file)
    print(diff)


def generate_diff(file_path1, file_path2):
    # print(file_path1, file_path2)
    first_file = json.load(open(file_path1))
    # print(first_file['host'])
    second_file = json.load(open(file_path2))
    key_list = making_keys_list(first_file, second_file)
    result = '{\n'
    # print(key_list)
    no_changes_string = '    {}: {}\n'
    add_key_string = '  + {}: {}\n'
    delete_key_string = '  - {}: {}\n'
    for key in key_list:
        if first_file.get(key) == second_file.get(key):
            result += (no_changes_string.format(key, converte_output(second_file[key])))
            continue
        if first_file.get(key) is None:
            result += (add_key_string.format(key, converte_output(second_file[key])))
            continue
        if second_file.get(key) is None:
            result += (delete_key_string.format(key, converte_output(first_file[key])))
            continue
        if first_file.get(key) != second_file.get(key):
            result += (delete_key_string.format(key, converte_output(first_file[key])))
            result += (add_key_string.format(key, converte_output(second_file[key])))
    # print(second_file)
    result += '}'
    return result


def making_keys_list(first_file, second_file):
    key_set = set()
    for key in first_file:
        key_set.add(key)
    for key in second_file:
        key_set.add(key)
    # print(key_set)
    key_list = list(key_set)
    key_list.sort()
    return key_list


def converte_output(output):
    if output is True:
        output = 'true'
    if output is False:
        output = 'false'
    return str(output)


if __name__ == '__main__':
    main()
