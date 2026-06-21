# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import hashlib
from app_runtime import auth_check


async def BenchmarkTest79176(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = '%s' % str(auth_header)
    auth_check('user', hashlib.sha256(str(data).encode()).hexdigest())
    return {"updated": True}
