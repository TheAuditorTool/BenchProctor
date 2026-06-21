# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import hashlib
from app_runtime import auth_check


async def BenchmarkTest02372(request: Request):
    user_id = request.query_params.get('id', '')
    data = '%s' % (user_id,)
    auth_check('user', hashlib.sha256(str(data).encode()).hexdigest())
    return {"updated": True}
