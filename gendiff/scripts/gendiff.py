#!/usr/bin/env python

import argparse


def main():
    #print("Hello!")
    parser = argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')
    parser.add_argument('file', metavar='first_file')
    parser.add_argument('file', metavar='second_file')
    parser.add_argument('-f','--format', help='set format of output')
    args = parser.parse_args()
    print(args.accumulate(args.integers))

if __name__ == '__main__':
    main()
