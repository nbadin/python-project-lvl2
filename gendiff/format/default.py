from gendiff.constants import (
    ADDED,
    REMOVED,
    NESTED,
    MODIFIED,
    EQUAL
)

STATUSES = {
    ADDED: '  + ',
    REMOVED: '  - ',
    EQUAL: '    ',
    NESTED: '    '
}


def stylish(diff, depth=0):
    result = []
    indent = '    ' * depth

    for key, data in diff.items():
        status, value = data[0], data[1:]
        if status == NESTED:
            value = stylish(value[0], depth + 1)
            result.append(f'{indent}{STATUSES[EQUAL]}{key}: {value}')

        elif status == MODIFIED:
            old_value = render_value(value[0], depth + 1)
            new_value = render_value(value[1], depth + 1)
            result.append(f'{indent}{STATUSES[REMOVED]}{key}: {old_value}')
            result.append(f'{indent}{STATUSES[ADDED]}{key}: {new_value}')

        else:
            value = render_value(value[0], depth + 1)
            result.append(f'{indent}{STATUSES[status]}{key}: {value}')

    return '{\n' + '\n'.join(result) + '\n' + indent + '}'


def render_value(value, depth):

    if isinstance(value, bool):
        return str(value).lower()

    elif value is None:
        return 'null'

    elif isinstance(value, dict):
        return dict_to_string(value, depth)

    else:
        return value


def dict_to_string(object, depth=0):
    result = []
    indent = '    ' * depth

    for key, value in object.items():
        if isinstance(value, dict):
            value = dict_to_string(value, depth + 1)
        else:
            value
        result.append(
            f'{indent}    {key}: {value}'
        )

    return '{\n' + '\n'.join(result) + '\n' + indent + '}'
