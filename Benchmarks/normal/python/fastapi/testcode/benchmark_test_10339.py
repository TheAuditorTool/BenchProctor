# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import hashlib
from app_runtime import auth_check


async def BenchmarkTest10339(request: Request):
    origin_value = request.headers.get('origin', '')
    if origin_value:
        data = origin_value
    else:
        data = ''
    auth_check('user', hashlib.sha256(str(data).encode()).hexdigest())
    return {"updated": True}
