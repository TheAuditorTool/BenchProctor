# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from urllib.parse import unquote
from app_runtime import auth_check


async def BenchmarkTest01417(request: Request):
    referer_value = request.headers.get('referer', '')
    data = unquote(referer_value)
    auth_check('user', data)
    return {"updated": True}
