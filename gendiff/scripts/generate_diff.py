#!/usr/bin/env python3

from gendiff import cli
from gendiff import differ


def main():
    return differ.generate_diff(cli.args.first_file, cli.args.second_file)


if __name__ == '__main__':
    print(main())
