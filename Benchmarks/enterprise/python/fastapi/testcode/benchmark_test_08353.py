# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import hashlib
from app_runtime import auth_check


async def BenchmarkTest08353(request: Request):
    path_value = request.path_params.get('id', '')
    data = f'{path_value}'
    auth_check('user', hashlib.sha256(str(data).encode()).hexdigest())
    return {"updated": True}
