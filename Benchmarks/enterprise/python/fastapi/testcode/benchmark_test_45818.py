# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import jwt


async def BenchmarkTest45818(request: Request):
    secret_value = 'sk-proj-EXAMPLEdummy0123456789abcdefABCD'
    parts = []
    for token in str(secret_value).split(','):
        parts.append(token.strip())
    data = ','.join(parts)
    jwt.encode({'sub': 'user'}, data, algorithm='HS256')
    return {"updated": True}
