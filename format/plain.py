def plain(diff_struct, way=''):
    result_string = ''
    for item in diff_struct:
        way_to_current = way + item['name']
        if isinstance(item.get('children'), list):
            way_to_current += '.'
            result_string += plain(item['children'], way_to_current)
        else:
            if item['status'] == 'same':
                continue
            action_text = make_action_string(item['status'])
            value = make_value_text(item)
            if item['status'] == 'del':
                result_string += 'Property \'{}\' {}\n'.format(way_to_current, action_text)
            else:
                result_string += 'Property \'{}\' {} {}\n'.format(way_to_current, action_text, value)
    return result_string


def make_action_string(status):
    result = ''
    if status == 'add':
        result += 'was added with value:'
    elif status == 'del':
        result += 'was removed'
    elif status == 'change':
        result += 'was updated.'
    return result


def make_value_text(item):
    status = item['status']
    if status == 'change':
        result = 'From {} to {}'.format(format_value(item['old_value']), format_value(item['new_value']))
    elif status == 'del':
        result = ''
    elif status == 'add':
        result = format_value(item['value'])
    else:
        result = format_value(item['value'])
    return result


def format_value(value):
    if isinstance(value, dict):
        return '[complex value]'
    elif isinstance(value, str):
        return '\'{}\''.format(value)
    elif isinstance(value, bool):
        if value is False:
            return 'false'
        elif value is True:
            return 'true'
    elif value is None:
        return 'null'
    elif isinstance(value, int):
        return '{}'.format(value)
