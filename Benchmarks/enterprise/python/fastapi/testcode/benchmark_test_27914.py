# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import jwt


async def BenchmarkTest27914(request: Request):
    secret_value = 'config_secret_test_abc123'
    data = f'{secret_value:.200s}'
    jwt.encode({'sub': 'user'}, data, algorithm='HS256')
    return {"updated": True}
