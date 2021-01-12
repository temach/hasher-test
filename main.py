#!/usr/bin/env python3
import argparse
from pathlib import Path
from pprint import pprint
from hasher import Hasher

parser = argparse.ArgumentParser(
    description="Hashes data"
)

parser.add_argument(
    'wordfile',
    type=Path,
    help="path to file with english words"
)

parser.add_argument(
    'input',
    type=str,
    help="String to hash"
)

args = parser.parse_args()


def main():
    hasher = Hasher(args.wordfile, nwords=3, delimeter="-")
    pprint(hasher.process(args.input))


if __name__ == "__main__":
    main()
