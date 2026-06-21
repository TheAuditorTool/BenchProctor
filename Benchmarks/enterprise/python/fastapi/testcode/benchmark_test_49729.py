# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import auth_check


async def BenchmarkTest49729(request: Request):
    user_id = request.query_params.get('id', '')
    data = ' '.join(str(user_id).split())
    auth_check('user', data)
    return {"updated": True}
