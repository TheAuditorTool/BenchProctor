# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import auth_check


async def BenchmarkTest03122(request: Request):
    user_id = request.query_params.get('id', '')
    data = f'{user_id:.200s}'
    auth_check('user', data)
    return {"updated": True}
