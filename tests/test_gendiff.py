from cgitb import reset
from unittest import result
import pytest
from gendiff.scripts.gendiff import generate_diff


def test_json():
    result_json = open('tests/fixtures/result_test_json.txt', 'r')
    assert generate_diff('tests/fixtures/file1.json', 'tests/fixtures/file2.json') == result_json.read()
