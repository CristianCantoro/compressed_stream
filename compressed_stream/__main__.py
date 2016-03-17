"""A simple command-line utility to process streams of compressed files."""

# Inspired by mediawiki-utilities by halfak et al.
# See:
# https://github.com/mediawiki-utilities/python-mediawiki-utilities/

import csv
import argparse
import pathlib

from .functions import open_file, file


def get_args():
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        prog='decompresscat',
        description=__doc__,
    )
    parser.add_argument(
        'files',
        metavar='FILE',
        type=pathlib.Path,
        nargs='+',
        help='CSV file to parse. It accepts only 7z.',
    )
    parser.add_argument(
        '--quiet', '-q',
        action='store_true',
        help="Don't write any output",
    )
    parser.add_argument(
        '--csv',
        action='store_true',
        help="Read file with CSV reader",
    )

    parsed_args = parser.parse_args()

    return parsed_args


def main():
    """Main function."""
    args = get_args()

    for infile in args.files:

        csv_file = open_file(str(infile))

        if args.csv:
            reader = csv.reader(csv_file)
            end = '\n'
            lines = ('\t'.join(row) for row in reader)

        else:
            reader = csv_file
            end = ''
            lines = reader

        for line in lines:
            if not args.quiet:
                print(line, end=end)

if __name__ == '__main__':
    main()
