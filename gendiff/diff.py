from gendiff.parcer import parse_files
from format.plain import plain
from format.json import json_format
from format.stylish import stylish


def generate_diff(file_path1, file_path2, format='stylish'):
    # Generates diff string in different formats
    first_dict, second_dict = parse_files(file_path1, file_path2)
    full_dict = _make_full_dict(first_dict, second_dict)
    diff_struct = _generate_diff_struct(full_dict, first_dict, second_dict)
    # print(diff_struct)
    format = _set_format_func(format)
    diff_string = format(diff_struct)
    # FIXME
    # fix func plain() in plain module to remove this block
    if format == plain:
        # removing last '\n' from result in plain format
        diff_string = diff_string[:-1]
    return diff_string


def _set_format_func(format):
    if format == 'plain':
        format = plain
    if format == 'json':
        format = json_format
    if format == 'stylish':
        format = stylish
    return format


def _make_full_dict(first_dict, second_dict):
    # make full dict to get all keys by updating from first and second dict, values doesn't matter
    full_dict = {}
    if isinstance(first_dict, dict):
        full_dict.update(first_dict)
    if isinstance(second_dict, dict):
        full_dict.update(second_dict)
    for key in full_dict:
        if isinstance(first_dict.get(key), dict) and isinstance(second_dict.get(key), dict):
            full_dict[key] = _make_full_dict(first_dict.get(key), second_dict.get(key))
    return full_dict


def _generate_diff_struct(full_dict, first_dict, second_dict):
    diff_struct = []
    for key in full_dict:
        unit = {}
        unit['name'] = key
        if key not in first_dict:
            unit['status'] = '+'
        elif key not in second_dict:
            unit['status'] = '-'
        else:
            unit['status'] = ' '
        if isinstance(first_dict.get(key), dict) and isinstance(second_dict.get(key), dict):
            unit['children'] = _generate_diff_struct(full_dict[key], first_dict[key], second_dict[key])
        else:
            if unit['status'] == '+':
                unit['value'] = second_dict.get(key)
            elif unit['status'] == '-':
                unit['value'] = first_dict.get(key)
            elif first_dict.get(key) == second_dict.get(key):
                unit['value'] = first_dict.get(key)
            elif first_dict.get(key) != second_dict.get(key):
                # TODO
                # make status arrangements in one place if possible
                unit['status'] = '-+'
                unit['old_value'] = first_dict.get(key)
                unit['value'] = second_dict.get(key)
        diff_struct.append(unit)
        diff_struct.sort(key=_sort_by_name)
    return diff_struct


def _sort_by_name(unit):
    return unit['name']
