#!/usr/bin/python3
"""This script reads stdin line by line and computes metrics."""

import sys


if __name__ == "__main__":
    def print_statistics(total_size, status_count):
        """Prints input to stdout."""

        print("File size: {}".format(total_size))

        sorted_status_codes = sorted(status_count.items())

        for code, count in sorted_status_codes:
            print("{}: {}".format(code, count))

    total_size = 0
    status_count = {200: 0, 301: 0, 400: 0, 401: 0,
                    403: 0, 404: 0, 405: 0, 500: 0}

    try:
        line_counter = 0

        for line in sys.stdin:
            line = line.strip()
            parts = line.split(" ")
            line_counter += 1
            print(parts)

            if len(parts) == 9:
                try:
                    status_code = int(parts[-2])

                    if status_code not in status_count:
                        continue
                except ValueError:
                    line_counter -= 1
                    continue

                try:
                    file_size = int(parts[-1])
                except ValueError:
                    line_counter -= 1
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
