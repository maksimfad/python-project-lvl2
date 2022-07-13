# import imp
from gendiff.parcer import parcing_files
from format.plain import plain
from format.json import json_format
from format.formatter import stylish
import json


def generate_diff(file_path1, file_path2, format=stylish):
    first_file, second_file = parcing_files(file_path1, file_path2)
    diff_struct = diff(first_file, second_file)
    # print(diff_struct)
    if format == 'plain':
        format = plain
    if format == 'json':
        format = json_format
    if format == 'stylish':
        format = stylish
    result_text = format(diff_struct)
    if format == plain:
        result_text = result_text[:-1]
    return result_text


def diff(first_dict, second_dict):
    def make_full_dict(first_dict, second_dict):
        full_dict = {}
        if isinstance(first_dict, dict):
            full_dict.update(first_dict)
        if isinstance(second_dict, dict):
            full_dict.update(second_dict)
        for key in full_dict:
            if isinstance(full_dict.get(key), dict) and isinstance(first_dict.get(key), dict) and isinstance(second_dict.get(key), dict):
                full_dict[key] = make_full_dict(first_dict.get(key), second_dict.get(key))
        return full_dict
    full_dict = make_full_dict(first_dict, second_dict)
    print('\n')
    diff_struct = adding_units(full_dict, first_dict, second_dict)
    # with open("tests/fixtures/result.json", "w") as write_file:
        # json.dump(diff_struct, write_file)
    # print(json.dumps(diff_struct))
    return diff_struct

def adding_units(full_dict, first_dict, second_dict):
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
            unit['children'] = adding_units(full_dict[key], first_dict[key], second_dict[key])
        else:
            if key not in first_dict:
                unit['status'] = 'add'
                unit['new_value'] = second_dict[key]
            elif key not in second_dict:
                unit['status'] = 'del'
                unit['old_value'] = first_dict[key]
            elif first_dict.get(key) == second_dict.get(key):
                unit['status'] = 'same'
                unit['old_value'] = first_dict[key]
                unit['new_value'] = second_dict[key]
            else:
                unit['status'] = 'change'
                unit['old_value'] = first_dict.get((key))
                unit['new_value'] = second_dict.get(key)
        diff_struct.append(unit)
    return diff_struct