import json


def json_format(diff_struct):
    # out_file = open('tests/fixtures/result.json', 'w')
    # json.dump(diff_struct, out_file)
    return json.dumps(diff_struct)
