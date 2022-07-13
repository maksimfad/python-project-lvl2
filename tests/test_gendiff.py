from gendiff.scripts.gendiff import generate_diff
from format.formatter import converte
from format.formatter import stylish
from format.plain import plain
from format.json import json_format


def test_generate_diff_json():
    result = open('tests/fixtures/result_test.txt', 'r').read()
    assert generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json', stylish) == result


def test_generate_diff_yml():
    result = open('tests/fixtures/result_test.txt', 'r').read()
    assert generate_diff('tests/fixtures/file1.yml', 'tests/fixtures/file2.yml', stylish) == result


def test_generate_diff_yml_json():
    result = open('tests/fixtures/result_test.txt', 'r').read()
    assert generate_diff('tests/fixtures/file1.yml', 'tests/fixtures/file2.json', stylish) == result
    assert generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.yml', stylish) == result


def test_generate_diff_plain_format():
    result = open('tests/fixtures/result_plain.txt', 'r').read()
    assert generate_diff('tests/fixtures/file1.yml', 'tests/fixtures/file2.yml', plain) == result


def test_generate_diff_json_format():
    result = open('tests/fixtures/result.json', 'r').read()
    assert generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.yml', json_format) == result


def test_converte():
    result = 'true'
    assert converte(True) == result
