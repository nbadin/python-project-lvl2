from gendiff.gendiff import generate_diff
import os
import pytest


@pytest.fixture
def expected_stylish():
    expected = []
    with open(os.path.abspath('./tests/fixtures/expected_stylish.txt')) as result:
        for line in result:
            expected.append(line)
    return ''.join(expected)


def test_gendiff_with_json(expected_stylish):
    assert generate_diff('./tests/fixtures/file1.json', './tests/fixtures/file2.json') == expected_stylish


def test_gendiff_with_yaml(expected_stylish):
    assert generate_diff('./tests/fixtures/file1.yaml', './tests/fixtures/file2.yml') == expected_stylish


def test_gendiff_with_json_and_yaml(expected_stylish):
    assert generate_diff('./tests/fixtures/file1.yaml', './tests/fixtures/file2.json', 'stylish') == expected_stylish
