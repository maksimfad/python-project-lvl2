from gendiff.parcer import parcing_files
from format.plain import plain
from format.json import json_format
from format.formatter import stylish


def generate_diff(file_path1, file_path2, format=stylish):
    # Generates diff string in different formats
    first_dict, second_dict = parcing_files(file_path1, file_path2)
    full_dict = make_full_dict(first_dict, second_dict)
    diff_struct = generate_diff_struct(full_dict, first_dict, second_dict)
    # print(diff_struct)
    if format == 'plain':
        format = plain
    if format == 'json':
        format = json_format
    if format == 'stylish':
        format = stylish
    result_text = format(diff_struct)
    # FIXME
    # fix func plain() in plain module to remove this block
    if format == plain:
        # removing last '\n' from result in plain format
        result_text = result_text[:-1]
    return result_text


def make_full_dict(first_dict, second_dict):
    # make full dict to get all keys by updating from first and second dict, values doesn't matter
    full_dict = {}
    if isinstance(first_dict, dict):
        full_dict.update(first_dict)
    if isinstance(second_dict, dict):
        full_dict.update(second_dict)
    for key in full_dict:
        if isinstance(first_dict.get(key), dict) and isinstance(second_dict.get(key), dict):
            full_dict[key] = make_full_dict(first_dict.get(key), second_dict.get(key))
    return full_dict


def generate_diff_struct(full_dict, first_dict, second_dict):
    diff_struct = []
    for key in full_dict:
        unit = {}
        unit['name'] = key
        if key not in first_dict:
            unit['status'] = 'add'
        elif key not in second_dict:
            unit['status'] = 'del'
        else:
            unit['status'] = 'same'
        if isinstance(first_dict.get(key), dict) and isinstance(second_dict.get(key), dict):
            unit['children'] = generate_diff_struct(full_dict[key], first_dict[key], second_dict[key])
        else:
            if unit['status'] == 'add':
                unit['value'] = second_dict.get(key)
            elif unit['status'] == 'del':
                unit['value'] = first_dict.get(key)
            elif first_dict.get(key) == second_dict.get(key):
                unit['value'] = first_dict.get(key)
            elif first_dict.get(key) != second_dict.get(key):
                # TODO
                # make status arrangements in one place if possible
                unit['status'] = 'change'
                unit['old_value'] = first_dict.get(key)
                unit['new_value'] = second_dict.get(key)
        diff_struct.append(unit)
        diff_struct.sort(key=sorting)
    return diff_struct

def sorting(unit):
    return unit['name']
