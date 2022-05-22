from gendiff.gendiff import generate_diff
import os
import pytest


expected = []
with open(os.path.abspath('./tests/fixtures/expected.txt')) as result:
    for line in result:
        expected.append(line)


def test_gendiff_with_json_files():
    assert generate_diff('./tests/fixtures/file1.json', './tests/fixtures/file2.json')  == ''.join(expected)


def test_gendiff_with_yaml_files():
    assert generate_diff('./tests/fixtures/file1.yaml', './tests/fixtures/file2.yml')  == ''.join(expected)