# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import jwt


async def BenchmarkTest59235(request: Request):
    secret_value = 'config_secret_test_abc123'
    data, _sep, _rest = str(secret_value).partition('\x00')
    jwt.encode({'sub': 'user'}, data, algorithm='HS256')
    return {"updated": True}
