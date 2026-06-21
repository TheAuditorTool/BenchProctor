# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import auth_check


async def BenchmarkTest62772(request: Request):
    secret_value = 'sk-proj-EXAMPLEdummy0123456789abcdefABCD'
    if secret_value:
        data = secret_value
    else:
        data = ''
    auth_check('user', data)
    return {"updated": True}
