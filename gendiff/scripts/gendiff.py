import argparse
from gendiff.gendiff import generate_diff


def main():
    parser = argparse.ArgumentParser(
        prog='gendiff',
        usage='gendiff [-h] [-f FORMAT] first_file second_file',
        description='Generate diff'
    )

    parser.add_argument('first_file', metavar='first_file', type=str)

    parser.add_argument('second_file', metavar='second_file', type=str)

    parser.add_argument(
        '-f',
        '--format',
        action='store',
        help='set format of output',
        default='stylish'
    )

    args = parser.parse_args()
    print(generate_diff(args.first_file, args.second_file, args.format))


if __name__ == '__main__':
    main()
