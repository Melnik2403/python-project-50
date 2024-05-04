#!/usr/bin/env python3

import argparse
from gendiff import differ


parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')
parser.add_argument('first_file')
parser.add_argument('second_file')
args = parser.parse_args()


def main(file1, file2):
    return differ.generate_diff(file1, file2)


if __name__ == '__main__':
    print(main(args.first_file, args.second_file))
