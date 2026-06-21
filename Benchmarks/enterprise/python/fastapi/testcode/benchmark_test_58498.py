# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import auth_check


def relay_value(value):
    return value

async def BenchmarkTest58498(request: Request):
    user_id = request.query_params.get('id', '')
    data = relay_value(user_id)
    auth_check('user', data)
    return {"updated": True}
