# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import jwt


async def BenchmarkTest68106(request: Request):
    secret_value = {'secret': 'p4ssw0rd_test_xyz'}['secret']
    parts = str(secret_value).split(',')
    data = ','.join(parts)
    jwt.encode({'sub': 'user'}, data, algorithm='HS256')
    return {"updated": True}
