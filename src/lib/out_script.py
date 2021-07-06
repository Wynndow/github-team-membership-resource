#!/usr/bin/env python

import json

from .utils.util import eprint


def main():
    eprint("Out not supported")
    output = {
        "version": {"hash": "none"},
        "metadata": []
    }
    print(json.dumps(output))


if __name__ == '__main__':
    main()

