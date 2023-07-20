#!/usr/bin/python3
'''Write a script that reads stdin line by line and computes metrics:

Input format: <IP Address> - [<date>] "GET /projects/260 HTTP/1.1"
<status code> <file size> (if the format is not this one, the line must
be skipped)
After every 10 lines and/or a keyboard interruption (CTRL + C), print these
statistics from the beginning:
Total file size: File size: <total size>
where <total size> is the sum of all previous <file size>
(see input format above)
Number of lines by status code:
possible status code: 200, 301, 400, 401, 403, 404, 405 and 500
if a status code doesn’t appear or is not an integer, don’t print anything
for this status code
format: <status code>: <number>
status codes should be printed in ascending order
Warning: In this sample, you will have random value - it’s normal to not
have the same output as this one.
'''
import sys

if __name__ == '__main__':
    status_codes = {'200': 0, '301': 0, '400': 0, '401': 0,
                    '403': 0, '404': 0, '405': 0, '500': 0}
    file_size = 0
    count = 0

    def print_stats():
        '''Prints the stats'''
        print('File size: {}'.format(file_size))
        for key in sorted(status_codes.keys()):
            if status_codes[key] != 0:
                print('{}: {}'.format(key, status_codes[key]))

    try:
        for line in sys.stdin:
            count += 1
            data = line.split()
            try:
                file_size += int(data[-1])
            except BaseException:
                pass
            try:
                status_codes[data[-2]] += 1
            except BaseException:
                pass
            if count % 10 == 0:
                print_stats()
    except KeyboardInterrupt:
        print_stats()
        raise
    print_stats()
