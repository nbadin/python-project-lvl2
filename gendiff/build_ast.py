from gendiff.constants import NESTED, ADDED, REMOVED, EQUAL, MODIFIED


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
