from cgitb import reset
from format.formatter import sorting


def plain(diff_struct, way=''):
    diff_struct.sort(key=sorting)
    result_string = ''
    for item in diff_struct:
        way_to_current = way + item['name']
        if isinstance(item.get('children'), list):
            way_to_current += '.'
            result_string += plain(item['children'], way_to_current)
        else:
            if item['status'] == 'same':
                continue
            action_text = action_status(item['status'])
            value = value_text(item)
            if item['status'] == 'del':
                result_string += 'Property \'{}\' {}\n'.format(way_to_current, action_text)
            else:
                result_string += 'Property \'{}\' {} {}\n'.format(way_to_current, action_text, value)
    return result_string


def action_status(status):
    result = ''
    if status == 'add':
        result += 'was added with value:'
    elif status == 'del':
        result += 'was removed'
    elif status == 'change':
        result += 'was updated.'
    return result


def value_text(item):
    status = item['status']
    if status == 'change':
        result = 'From {} to {}'.format(value_check(item['old_value']), value_check(item['new_value']))
    elif status == 'del':
        result = ''
    elif status == 'add':
        result = value_check(item['new_value'])
    else:
        result = value_check(item['old_value'])
    return result


def value_check(value):
    if isinstance(value, dict):
        return '[complex value]'
    elif isinstance(value, str):
        return '\'{}\''.format(value)
    elif isinstance(value, bool):
        if value == False:
            return 'false'
        elif value == True:
            return 'true'
    elif value == None:
        return 'null'
    elif isinstance(value, int):
        return '\'{}\''.format(value)
