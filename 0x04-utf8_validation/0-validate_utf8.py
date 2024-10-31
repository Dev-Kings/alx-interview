#!/usr/bin/python3
"""
Module that validates UTF-8 encoding """


def validUTF8(data):
    """
    Determines if a given dataset represents a valid UTF-8 encoding
    Args:
        data(List(int)): List of integers that rep bytes of the dataset
        Each integer rep 1 byte if data (8 least signigicant bits)
    Returns:
        bool: True if data is a valid UTF-8 encoding, else False."""

    num_bytes = 0

    for byte in data:
        # if byte starts with 0, then it rep a single-byte character
        if num_bytes == 0:
            if byte >> 7 == 0b0:
                continue
            # Count the number of leading 1's to det no of bytes in character
            elif byte >> 5 == 0b110:
                num_bytes = 1
            elif byte >> 4 == 0b1110:
                num_bytes = 2
            elif byte >> 3 == 0b11110:
                num_bytes = 3
            else:
                return False
        else:
            # If a byte doesn't start with 10, it's not valid continuation byte
            if byte >> 6 != 0b10:
                return False
            num_bytes -= 1

    # If there are leftover bytes, it means the data is incomplete
    return num_bytes == 0
