from cgitb import reset
from unittest import result
import pytest
import json
from gendiff.scripts.gendiff import generate_diff
from gendiff.scripts.gendiff import making_keys_list
from gendiff.scripts.gendiff import converte


def test_json():
    result_json = open('tests/fixtures/result_test_json.txt', 'r')
    assert generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json') == result_json.read()


def test_making_keys_list():
    first_file = json.load(open('tests/fixtures/file1.json'))
    second_file = json.load(open('tests/fixtures/file2.json'))
    result =['follow', 'host', 'proxy', 'timeout', 'verbose']
    assert making_keys_list(first_file, second_file) == result

def test_converte():
    result = 'true'
    assert converte(True) == result
