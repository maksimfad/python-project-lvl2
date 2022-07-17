def plain(diff_struct, way=''):
    result_string = ''
    for item in diff_struct:
        way_to_current = way + item['name']
        if isinstance(item.get('children'), list):
            way_to_current += '.'
            result_string += plain(item['children'], way_to_current)
        else:
            if item['status'] == ' ':
                continue
            action_text = _make_action_text(item['status'])
            value = _make_value_text(item)
            if item['status'] == '-':
                result_string += 'Property \'{}\' {}\n'.format(way_to_current, action_text)
            else:
                result_string += 'Property \'{}\' {} {}\n'.format(way_to_current, action_text, value)
    return result_string


def _make_action_text(status):
    result = ''
    if status == '+':
        result += 'was added with value:'
    elif status == '-':
        result += 'was removed'
    elif status == '-+':
        result += 'was updated.'
    return result


def _make_value_text(item):
    status = item['status']
    value = _format_value(item.get('value'))
    old_value = _format_value(item.get('old_value'))
    if status == '-+':
        result = f'From {old_value} to {value}'
    elif status == '-':
        result = ''
    else:
        result = value
    return result


def _format_value(value):
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
