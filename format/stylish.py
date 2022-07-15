def stylish(diff_struct, space=' ', times=2):
    result_string = '{\n'
    for key in diff_struct:
        name = key.get('name')
        if isinstance(key.get('children'), list):
            times += 2
            tabs = space * times
            result_string += '{}{}: '.format(tabs, name)
            result_string += stylish(key['children'], times=times + 2)
            result_string += '\n'
            times -= 2
        else:
            tabs = space * times
            status = key.get('status')
            if status == 'change':
                old_value = _format_value(key.get('old_value'), times)
                result_string += _format_string(tabs, '-', name, old_value)
                new_value = _format_value(key.get('new_value'), times)
                result_string += _format_string(tabs, '+', name, new_value)
            else:
                value = _format_value(key.get('value'), times)
                result_string += _format_string(tabs, status, name, value)
    times -= 2
    tabs = space * times
    result_string += (tabs + '}')
    return result_string


def _format_string(tabs, sign, name, value):
    return f'{tabs}{sign} {name}: {value}\n'


def _format_value(value, times):
    if isinstance(value, dict):
        return_string = _format_dict_value(value, times)
    else:
        if value is True:
            value = 'true'
        if isinstance(value, bool) and value is False:
            value = 'false'
        if value is None:
            value = 'null'
        return_string = str(value)
    return return_string


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
            formatted_value = _format_value(dict_value[key], times)
            return_string += f'{tabs}  {key}: {formatted_value}\n'
    times -= 2
    tabs = ' ' * times
    return_string += tabs + '}'
    return return_string
