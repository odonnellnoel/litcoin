#!/usr/bin/env python3

def validate_uint256(n):
    assert type(n) == int, 'type of `n` should be int'
    assert 0 <= n, '`n` may not be negative'
    assert n <= 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff, '`n` must fit within 256 bits'


def serialize_uint256(n):
    validate_uint256(n)
    return int.to_bytes(n, 32, byteorder='little', signed=False)


def deserialize_uint256(data, i=0):
    assert type(data) == bytes
    assert type(i) == int
    assert 0 <= i
    assert i + 32 <= len(data)
    return int.from_bytes(data[i:i+32], byteorder='little', signed=False)
