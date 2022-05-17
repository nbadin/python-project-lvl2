import json
import pathlib


def get_file(file_name):
    ext = pathlib.Path(file_name).suffix
    if ext == '.json':
        return json.load(open(file_name))


def generate_diff(first_path, second_path):
    result = []
    first_file = get_file(first_path)
    second_file = get_file(second_path)
    for key in sorted(set([*first_file.keys(), *second_file.keys()])):
        if key in first_file and key in second_file:
            if first_file[key] != second_file[key]:
                result.append(f'  - {key}: {first_file[key]}')
                result.append(f'  + {key}: {second_file[key]}')
            if first_file[key] == second_file[key]:
                result.append(f'    {key}: {first_file[key]}')
        if key in first_file and key not in second_file:
            result.append(f'  - {key}: {first_file[key]}')
        if key not in first_file and key in second_file:
            result.append(f'  + {key}: {second_file[key]}')

    
    return '\n'.join(['{', *result, '}'])


    