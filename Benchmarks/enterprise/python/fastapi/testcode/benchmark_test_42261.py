# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import auth_check


async def BenchmarkTest42261(request: Request):
    secret_value = 'sk-proj-EXAMPLEdummy0123456789abcdefABCD'
    parts = str(secret_value).split(',')
    data = ','.join(parts)
    auth_check('user', data)
    return {"updated": True}
