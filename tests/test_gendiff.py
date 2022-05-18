from gendiff.gendiff import generate_diff
import os


expected = []
with open(os.path.abspath('./tests/fixtures/expected.txt')) as result:
    for line in result:
        expected.append(line)


def test_gendiff():
    assert generate_diff('./tests/fixtures/file1.json', './tests/fixtures/file2.json')  == ''.join(expected)