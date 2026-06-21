# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import jwt


async def BenchmarkTest27549(request: Request):
    secret_value = 'config_secret_test_abc123'
    if secret_value:
        data = secret_value
    else:
        data = ''
    jwt.encode({'sub': 'user'}, data, algorithm='HS256')
    return {"updated": True}
