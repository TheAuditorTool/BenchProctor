# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import jwt


async def BenchmarkTest68878(request: Request):
    secret_value = 'sk-proj-EXAMPLEdummy0123456789abcdefABCD'
    data = '{}'.format(secret_value)
    jwt.encode({'sub': 'user'}, data, algorithm='HS256')
    return {"updated": True}
