#!/usr/bin/env python

from gendiff.parcer import parcing_arguments
from gendiff.gendiff import generate_diff
# from unittest import result


def main():
    args = parcing_arguments()
    diff = generate_diff(args.first_file, args.second_file, args.format)
    print(diff)


if __name__ == '__main__':
    main()
