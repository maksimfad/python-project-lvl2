import json


def json_format(diff_struct):
    # _make_json_dump(diff_struct)
    return json.dumps(diff_struct)


def _make_json_dump(diff_struct):
    out_file = open('tests/fixtures/result.json', 'w')
    json.dump(diff_struct, out_file)
