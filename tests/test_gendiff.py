from gendiff.scripts.gendiff import generate_diff


def test_generate_diff_json():
    result = open('tests/fixtures/result_test.txt', 'r').read()
    assert generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json') == result


def test_generate_diff_yml():
    result = open('tests/fixtures/result_test.txt', 'r').read()
    assert generate_diff('tests/fixtures/file1.yml', 'tests/fixtures/file2.yml') == result


def test_generate_diff_yml_json():
    result = open('tests/fixtures/result_test.txt', 'r').read()
    assert generate_diff('tests/fixtures/file1.yml', 'tests/fixtures/file2.json') == result
    assert generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.yml') == result


def test_generate_diff_stylish_format():
    result = open('tests/fixtures/result_test.txt', 'r').read()
    assert generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json', 'stylish') == result


def test_generate_diff_plain_format():
    result = open('tests/fixtures/result_plain.txt', 'r').read()
    assert generate_diff('tests/fixtures/file1.yml', 'tests/fixtures/file2.yml', 'plain') == result


def test_generate_diff_json_format():
    result = open('tests/fixtures/result.json', 'r').read()
    assert generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.yml', 'json') == result
