from cgitb import reset
from unittest import result
import pytest
import json
from gendiff.scripts.gendiff import generate_diff
from gendiff.scripts.gendiff import making_keys_list
from gendiff.scripts.gendiff import converte


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




def test_making_keys_list():
    first_file = json.load(open('tests/fixtures/file1.json'))
    second_file = json.load(open('tests/fixtures/file2.json'))
    result =['follow', 'host', 'proxy', 'timeout', 'verbose']
    assert making_keys_list(first_file, second_file) == result

def test_converte():
    result = 'true'
    assert converte(True) == result
