# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from urllib.parse import unquote
from starlette.responses import JSONResponse
from app_runtime import auth_check


async def BenchmarkTest60048(request: Request):
    referer_value = request.headers.get('referer', '')
    data = unquote(referer_value)
    if auth_check('user', str(data)):
        return JSONResponse({'authenticated': True}, status_code=200)
    return {"updated": True}
