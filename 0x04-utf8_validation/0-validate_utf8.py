#!/usr/bin/python3
"""UTF-8 Validation"""


def validUTF8(data):
    """Determines if a given data set represents a
    valid UTF-8 encoding"""

    def check_next_bytes(num_bytes):
        nonlocal i
        for _ in range(num_bytes):
            if i >= len(data) or (data[i] >> 6) != 0b10:
                return False
            i += 1
        return True

    i = 0
    while i < len(data):
        byte = data[i]
        if (byte >> 7) == 0:  # 1-byte character (0xxxxxxx)
            i += 1
        elif (byte >> 5) == 0b110:  # 2-byte character (110xxxxx)
            if not check_next_bytes(1):
                return False
        elif (byte >> 4) == 0b1110:  # 3-byte character (1110xxxx)
            if not check_next_bytes(2):
                return False
        elif (byte >> 3) == 0b11110:  # 4-byte character (11110xxx)
            if not check_next_bytes(3):
                return False
        else:
            return False
        i += 1

    return True
