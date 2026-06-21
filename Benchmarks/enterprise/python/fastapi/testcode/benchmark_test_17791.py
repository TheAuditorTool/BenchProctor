# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import jwt


async def BenchmarkTest17791(request: Request):
    secret_value = ['s3cr3t_key_test_xyz'][0]
    data, _sep, _rest = str(secret_value).partition('\x00')
    jwt.encode({'sub': 'user'}, data, algorithm='HS256')
    return {"updated": True}
