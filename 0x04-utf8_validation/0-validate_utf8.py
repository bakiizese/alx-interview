#!/usr/bin/python3
''' validate utf8 '''


def validUTF8(data):
    ''' validate  data '''
    try:
        bt = bytes(data)
        bt.decode('utf-8')
        return True
    except Exception:
        return False
