# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import auth_check


async def BenchmarkTest20512(request: Request):
    path_value = request.path_params.get('id', '')
    data = '{}'.format(path_value)
    auth_check('user', data)
    return {"updated": True}
