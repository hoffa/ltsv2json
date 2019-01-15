#!/usr/bin/env python

import json
import signal
import sys


def main():
    signal.signal(signal.SIGPIPE, signal.SIG_DFL)
    while True:
        line = sys.stdin.readline()
        try:
            record = dict(map(lambda f: f.split(":", 1), line.strip().split("\t")))
            print(json.dumps(record, separators=(",", ":")))
        except ValueError:
            pass


if __name__ == "__main__":
    main()
