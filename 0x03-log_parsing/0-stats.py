#!/usr/bin/python3
'''Log parsing'''
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
