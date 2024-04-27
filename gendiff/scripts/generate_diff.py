#!/usr/bin/env python3

import argparse
from gendiff import gendiff


parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')
parser.add_argument('first_file')
parser.add_argument('second_file')
args = parser.parse_args()


def main(file_path1, file_path2):
    diff = gendiff.differ(file_path1, file_path2)
    return gendiff.formatter(diff)


if __name__ == '__main__':
    print(main(args.first_file, args.second_file))
