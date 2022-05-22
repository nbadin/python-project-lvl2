import json
import pathlib
import yaml
from gendiff.build_ast import build_ast
from gendiff.format.default import stylish
from gendiff.format.plain import plain


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
