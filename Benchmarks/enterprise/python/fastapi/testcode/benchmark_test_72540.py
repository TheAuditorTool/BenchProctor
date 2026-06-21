# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import hashlib
from app_runtime import auth_check


async def BenchmarkTest72540(request: Request):
    ua_value = request.headers.get('user-agent', '')
    auth_check('user', hashlib.sha256(str(ua_value).encode()).hexdigest())
    return {"updated": True}
