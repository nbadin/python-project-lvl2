import json
import pathlib
import yaml
from gendiff.format.default import stylish
from gendiff.format.plain import plain
from gendiff.format.json import render
from gendiff.statuses import (
    ADDED,
    MODIFIED,
    REMOVED,
    EQUAL,
    NESTED
)


def get_file(file_name):
    ext = pathlib.Path(file_name).suffix
    if ext == '.json':
        return json.load(open(file_name))
    if ext == '.yaml' or ext == '.yml':
        return yaml.safe_load(open(file_name))
    else:
        raise Exception('Unsupported output format')


def generate_diff(first_path, second_path, format='stylish'):
    first_file = get_file(first_path)
    second_file = get_file(second_path)
    if format == 'stylish':
        return stylish(build_ast(first_file, second_file))
    if format == 'plain':
        return plain(build_ast(first_file, second_file))
    if format == 'json':
        return render(build_ast(first_file, second_file))


def build_ast(first_file, second_file):  # noqa: C901
    diff = {}
    keys = sorted(first_file.keys() | second_file.keys())
    for key in keys:
        if key not in second_file:
            diff[key] = (REMOVED, first_file[key])
        elif key not in first_file:
            diff[key] = (ADDED, second_file[key])
        elif (isinstance(first_file[key], dict) and  # noqa: W504
                isinstance(second_file[key], dict)):
            diff[key] = (NESTED, build_ast(first_file[key], second_file[key]))
        elif first_file[key] != second_file[key]:
            diff[key] = (MODIFIED, first_file[key], second_file[key])
        elif first_file[key] == second_file[key]:
            diff[key] = (EQUAL, first_file[key])
    return diff
