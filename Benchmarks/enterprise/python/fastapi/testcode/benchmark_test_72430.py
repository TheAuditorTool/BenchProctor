# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import jwt


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest72430(request: Request):
    secret_value = {'secret': 'p4ssw0rd_test_xyz'}['secret']
    reader = make_reader(secret_value)
    data = reader()
    jwt.encode({'sub': 'user'}, data, algorithm='HS256')
    return {"updated": True}
