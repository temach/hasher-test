import json
import argparse
from pathlib import Path
from math import ceil


class Hasher():
    """Will hash a given object to a string of meaningful english words"""

    def __init__(self, filepath: Path, nwords: int = 3, delimeter: str = ""):
        self._nwords = nwords
        self._delimeter = delimeter
        with open(filepath, encoding="utf-8") as f:
            self._alphabet = f.read().split()
        # pprint(self.alphabet[:10])

    @staticmethod
    def _chunks(data, n):
        for i in range(0, len(data), n):
            yield data[i:i + n]

    def process(self, input) -> str:
        """Inspired by http://www.cse.yorku.ca/~oz/hash.html"""
        s = json.dumps(input)
        chunksize = ceil(len(s) / self._nwords)
        hashval = []
        index = 0
        for chunk in Hasher._chunks(s, chunksize):
            for ch in chunk:
                index = (ord(ch) + 31 * index)
            index %= len(self._alphabet)
            hashval.append(self._alphabet[index].title())
        return self._delimeter.join(hashval)
