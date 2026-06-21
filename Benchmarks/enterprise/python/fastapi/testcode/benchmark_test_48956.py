# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from urllib.parse import unquote
from app_runtime import auth_check


async def BenchmarkTest48956(request: Request):
    path_value = request.path_params.get('id', '')
    data = unquote(path_value)
    auth_check('user', data)
    return {"updated": True}
