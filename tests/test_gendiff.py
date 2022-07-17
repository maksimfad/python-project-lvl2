from gendiff.scripts.gendiff import generate_diff
from gendiff.parcer import parse_files
import json
import yaml


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


def test_parse_files():
    result1 = json.load(open('tests/fixtures/file1.json'))
    result2 = yaml.load(open('tests/fixtures/file1.yml'), Loader=yaml.SafeLoader)
    result = [result1, result2]
    assert parse_files('tests/fixtures/file1.yml', 'tests/fixtures/file1.json') == result
