#!/usr/bin/python3
"""
Python module that reads stdin line by line and computes metrics:"""
import sys


if __name__ == '__main__':
    # Initialize variables to store file size and status code counts
    file_size = [0]
    status_codes = {200: 0, 301: 0, 400: 0, 401: 0,
                    403: 0, 404: 0, 405: 0, 500: 0}

    def print_stats():
        """ Print the computed statistics """
        print('File size: {}'.format(file_size[0]))
        for key in sorted(status_codes.keys()):
            if status_codes[key]:
                print('{}: {}'.format(key, status_codes[key]))

    def parse_line(line):
        """
        Parses a line of log data and updates metrics.
        parameters:
            line (str): A line of log data. """

        try:
            # Split the line by spaces to extract status code and file size
            line = line[:-1]
            word = line.split(' ')
            # File size is last element on stdout
            file_size[0] += int(word[-1])
            # Status code is the second-to-last element
            status_code = int(word[-2])
            # Move through dictionary of status codes
            if status_code in status_codes:
                status_codes[status_code] += 1

        except BaseException:
            # Ignore lines with incorrect format
            pass

    linenum = 1
    try:
        # Iterate through each line of input from stdin
        for line in sys.stdin:
            parse_line(line)
            # Print statistics after every 10 lines
            if linenum % 10 == 0:
                print_stats()
            linenum += 1

    except KeyboardInterrupt:
        # Print final statistics in case of keyboard interruption
        print_stats()
        raise

    # Print final statistics
    print_stats()
