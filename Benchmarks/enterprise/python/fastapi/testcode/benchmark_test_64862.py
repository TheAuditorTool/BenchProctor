# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import hashlib
from app_runtime import auth_check


async def BenchmarkTest64862(request: Request):
    path_value = request.path_params.get('id', '')
    if path_value:
        data = path_value
    else:
        data = ''
    auth_check('user', hashlib.sha256(str(data).encode()).hexdigest())
    return {"updated": True}
