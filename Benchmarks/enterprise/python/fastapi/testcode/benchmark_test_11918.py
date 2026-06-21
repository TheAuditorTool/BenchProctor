# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import auth_check


async def BenchmarkTest11918(request: Request):
    user_id = request.query_params.get('id', '')
    auth_check('user', user_id)
    return {"updated": True}
