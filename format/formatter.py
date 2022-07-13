def stylish(diff_struct, space=' ', times=2):
    result_string = '{\n'
    diff_struct.sort(key=sorting)
    for key in diff_struct:
        name = key.get('name')
        if isinstance(key.get('children'), list):
            times += 2
            shift = space * times
            result_string += '{}{}: '.format(shift, name)
            result_string += stylish(key['children'], times=times + 2)
            result_string += '\n'
            times -= 2
        else:
            shift = space * times
            status = key.get('status')
            if status == 'same':
                result_string += '{}  {}: {}\n'.format(shift, name, style_value(key.get('new_value'), times))
            elif status == 'del':
                result_string += '{}- {}: {}\n'.format(shift, name, style_value(key.get('old_value'), times))
            elif status == 'add':
                result_string += '{}+ {}: {}\n'.format(shift, name, style_value(key.get('new_value'), times))
            elif status == 'change':
                result_string += '{}- {}: {}\n'.format(shift, name, style_value(key.get('old_value'), times))
                result_string += '{}+ {}: {}\n'.format(shift, name, style_value(key.get('new_value'), times))
    times -= 2
    shift = space * times
    result_string += (shift + '}')
    return result_string


def style_value(value, times):
    if isinstance(value, dict):
        return_string = format_dict_value(value, times)
    else:
        if value is True:
            value = 'true'
        if isinstance(value, bool) and value is False:
            value = 'false'
        if value is None:
            value = 'null'
        return_string = str(value)
    return return_string


def converte(output):
    if output is None:
        output = 'null'
    if output is True:
        output = 'true'
    if output is False:
        output = 'false'
    return str(output)


def sorting(unit):
    return unit['name']


def format_dict_value(dict_value, times):
    return_string = '{\n'
    times += 4
    shift = ' ' * times
    for key in dict_value:
        if isinstance(dict_value[key], dict):
            return_string += '{}  {}: '.format(shift, key)
            return_string += format_dict_value(dict_value[key], times)
            return_string += '\n'
        else:
            return_string += '{}  {}: {}\n'.format(shift, key, converte(dict_value[key]))
    times -= 2
    shift = ' ' * times
    return_string += shift + '}'
    return return_string
