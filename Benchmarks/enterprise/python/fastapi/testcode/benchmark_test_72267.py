# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from app_runtime import auth_check


async def BenchmarkTest72267(request: Request):
    origin_value = request.headers.get('origin', '')
    data, _sep, _rest = str(origin_value).partition('\x00')
    auth_check('user', data)
    return {"updated": True}
