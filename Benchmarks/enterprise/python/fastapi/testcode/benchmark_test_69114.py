# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import hashlib
from app_runtime import auth_check


async def BenchmarkTest69114(request: Request):
    referer_value = request.headers.get('referer', '')
    data = '{}'.format(referer_value)
    auth_check('user', hashlib.sha256(str(data).encode()).hexdigest())
    return {"updated": True}
