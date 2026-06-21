# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest47837(request: Request):
    origin_value = request.headers.get('origin', '')
    if str(origin_value).startswith('https://admin.internal/'):
        return JSONResponse({'authenticated': True}, status_code=200)
    return {"updated": True}
