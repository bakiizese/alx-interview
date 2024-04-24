#!/usr/bin/python3
"""
Main file for testing
"""

minOperations = __import__('0-minoperations').minOperations

n = 23
print("Min number of operations to reach {} char: {}".format(n, minOperations(n)))

n = 22
print("Min number of operations to reach {} char: {}".format(n, minOperations(n)))

