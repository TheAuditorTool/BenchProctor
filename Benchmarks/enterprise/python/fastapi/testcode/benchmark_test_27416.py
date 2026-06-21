# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import jwt


async def BenchmarkTest27416(request: Request):
    secret_value = ['s3cr3t_key_test_xyz'][0]
    if secret_value:
        data = secret_value
    else:
        data = ''
    jwt.encode({'sub': 'user'}, data, algorithm='HS256')
    return {"updated": True}
