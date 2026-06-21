# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import jwt


async def BenchmarkTest44164(request: Request):
    secret_value = {'secret': 'p4ssw0rd_test_xyz'}['secret']
    data = (lambda v: v.strip())(secret_value)
    jwt.encode({'sub': 'user'}, data, algorithm='HS256')
    return {"updated": True}
