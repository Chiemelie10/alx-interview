#!/usr/bin/python3
"""This script reads stdin line by line and computes metrics."""

import sys


def print_statistics(total_size, status_count):
    """Prints input to stdout."""

    print("File size: {}".format(total_size))

    sorted_status_codes = sorted(status_count.items())

    for code, count in sorted_status_codes:
        print("{}: {}".format(code, count))


def main():
    """ Main """
    total_size = 0
    status_count = {}

    try:
        line_counter = 0

        for line in sys.stdin:
            line = line.strip()
            parts = line.split()
            line_counter += 1

            if len(parts) >= 7:
                status_code = parts[-2]
                try:
                    file_size = int(parts[-1])
                except ValueError:
                    continue

                total_size += file_size

                if status_code in status_count:
                    status_count[status_code] += 1
                else:
                    status_count[status_code] = 1
            else:
                line_counter -= 1

            if line_counter % 10 == 0:
                print_statistics(total_size, status_count)
    except KeyboardInterrupt:
        print_statistics(total_size, status_count)
        sys.exit(0)


if __name__ == "__main__":
    main()
