def stylish(diff_struct, space=' ', times=2):
    diff_string = '{\n'
    for key in diff_struct:
        name = key.get('name')
        if isinstance(key.get('children'), list):
            times += 2
            tabs = space * times
            diff_string += '{}{}: '.format(tabs, name)
            diff_string += stylish(key['children'], times=times + 2)
            diff_string += '\n'
            times -= 2
        elif isinstance(key.get('value'), list):
            times += 2
            tabs = space * times
            diff_string += '{}{}: '.format(tabs, name[key])
            diff_string += stylish(key['value'], times=times + 2)
            diff_string += '\n'
            times -= 2
        else:
            tabs = space * times
            status = key.get('status')
            value = key.get('value')
            if status == '-+':
                old_value = key.get('old_value')
                diff_string += _format_string(times, '-', name, old_value)
                diff_string += _format_string(times, '+', name, value)
            else:
                diff_string += _format_string(times, status, name, value)
    times -= 2
    tabs = space * times
    diff_string += (tabs + '}')
    return diff_string


def _format_string(times, sign, name, value):
    tabs = ' ' * times
    if isinstance(value, dict):
        formatted_value = _format_dict_value(value, times)
    else:
        formatted_value = _format_value(value, times)
    return f'{tabs}{sign} {name}: {formatted_value}\n'


def _format_value(value, times=1):
    if value is True:
        value = 'true'
    if isinstance(value, bool) and value is False:
        value = 'false'
    if value is None:
        value = 'null'
    formatted_value = str(value)
    return formatted_value


def _format_dict_value(dict_value, times):
    return_string = '{\n'
    times += 4
    tabs = ' ' * times
    for key in dict_value:
        if isinstance(dict_value[key], dict):
            return_string += f'{tabs}  {key}: '
            return_string += _format_dict_value(dict_value[key], times)
            return_string += '\n'
        else:
            formatted_value = _format_value(dict_value[key])
            return_string += _format_string(times, ' ', key, formatted_value)
    times -= 2
    tabs = ' ' * times
    return_string += tabs + '}'
    return return_string
