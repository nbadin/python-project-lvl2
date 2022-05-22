from gendiff.constants import (
    ADDED,
    REMOVED,
    NESTED,
    MODIFIED
)


def plain(diff, path=[]):
    result = []
    for key, data in diff.items():
        status, value = data[0], data[1:]
        property_path = '.'.join([*path, key])

        if status == REMOVED:
            result.append(f'Property \'{property_path}\' was removed')
        
        if status == ADDED:
            value = render_value(value[0])
            result.append(
                f'Property \'{property_path}\' was added with value: {value}'
            )
        
        if status == MODIFIED:
            old_value = render_value(value[0])
            new_value = render_value(value[1])
            result.append(
                f'Property \'{property_path}\' was updated. From {old_value} to {new_value}'
            )
        
        if status == NESTED:
            new_path = [*path, key]
            result.append(plain(value[0], new_path))
    
    return '\n'.join(result)


def render_value(value):
    if isinstance(value, dict):
        return '[complex value]'
    if isinstance(value, str):
        return f'\'{value}\''
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return 'null'
    return value
