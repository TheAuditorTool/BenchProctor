# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import jwt


async def BenchmarkTest08539(request: Request):
    secret_value = ['s3cr3t_key_test_xyz'][0]
    parts = str(secret_value).split(',')
    data = ','.join(parts)
    jwt.encode({'sub': 'user'}, data, algorithm='HS256')
    return {"updated": True}
