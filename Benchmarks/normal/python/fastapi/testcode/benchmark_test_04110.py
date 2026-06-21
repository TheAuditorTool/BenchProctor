# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import jwt


async def BenchmarkTest04110(request: Request):
    secret_value = 'sk-proj-EXAMPLEdummy0123456789abcdefABCD'
    data = secret_value if secret_value else 'default'
    jwt.encode({'sub': 'user'}, data, algorithm='HS256')
    return {"updated": True}
