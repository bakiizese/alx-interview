#!/usr/bin/python3
''' validate utf8 '''


def validUTF8(data):
    ''' validation '''
    num_bytes = 0
    m_1 = 1 << 7
    m_2 = 1 << 6

    for bit in data:
        m_byte = 1 << 7
        if num_bytes == 0:
            while m_byte & bit:
                num_bytes += 1
                m_byte = m_byte >> 1
            if num_bytes == 0:
                continue
            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            if not (bit & m_1 and not (bit & m_2)):
                return False
        num_bytes -= 1
    if num_bytes == 0:
        return True

    return False
