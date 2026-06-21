# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import jwt


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

async def BenchmarkTest09161(request: Request):
    secret_value = {'secret': 'p4ssw0rd_test_xyz'}['secret']
    data = handle(secret_value)
    processed = data[:64]
    jwt.encode({'sub': 'user'}, processed, algorithm='HS256')
    return {"updated": True}
