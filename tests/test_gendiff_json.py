from gendiff.gendiff import generate_diff
import pytest
import os


@pytest.fixture
def expected_json():
    expected = []
    with open(os.path.abspath('./tests/fixtures/expected_json.txt')) as result:
        for line in result:
            expected.append(line)
    return ''.join(expected)


def test_gendiff_json(expected_json):
    assert generate_diff('./tests/fixtures/file1.json', './tests/fixtures/file2.json', 'json') == expected_json
    assert generate_diff('./tests/fixtures/file1.yaml', './tests/fixtures/file2.yml', 'json') == expected_json
    assert generate_diff('./tests/fixtures/file1.yaml', './tests/fixtures/file2.json', 'json') == expected_json
