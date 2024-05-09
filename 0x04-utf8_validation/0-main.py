#!/usr/bin/python3
"""
Main file for testing
"""

validUTF8 = __import__('0-validate_utf8').validUTF8

data = [65]
print(validUTF8(data))

data = [42]
print(validUTF8(data))

data = [0]
print(validUTF8(data))

