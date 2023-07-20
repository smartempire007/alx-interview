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
import signal

status_codes = {'200', '301', '400', '401', '403', '404', '405', '500'}
file_size_total = 0
status_code_counts = {code: 0 for code in status_codes}
line_count = 0


def print_statistics():
    '''Prints the statistics'''
    print("Total file size:", file_size_total)
    for code in sorted(status_codes, key=int):
        count = status_code_counts[code]
        if count > 0:
            print(f"{code}: {count}")


def signal_handler(sig, frame):
    '''Handles the SIGINT signal'''
    print_statistics()
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)

if __name__ == '__main__':
    try:
        for line in sys.stdin:
            line_count += 1
            if line_count % 10 == 0:
                print_statistics()

            parts = line.strip().split()
            if len(parts) != 10:
                continue

            ip, date, method, path, protocol, status_code, file_size = parts
            if not status_code.isdigit() or status_code not in status_codes:
                continue

            file_size_total += int(file_size)
            status_code_counts[status_code] += 1

    except KeyboardInterrupt:
        pass

    print_statistics()
