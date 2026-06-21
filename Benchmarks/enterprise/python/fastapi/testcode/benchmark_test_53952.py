# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import auth_check


async def BenchmarkTest53952(request: Request):
    origin_value = request.headers.get('origin', '')
    if origin_value:
        data = origin_value
    else:
        data = ''
    auth_check('user', data)
    return {"updated": True}
