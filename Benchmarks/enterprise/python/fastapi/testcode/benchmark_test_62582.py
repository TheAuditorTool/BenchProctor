# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest62582(request: Request):
    referer_value = request.headers.get('referer', '')
    if referer_value:
        data = referer_value
    else:
        data = ''
    if len(str(data)) >= 4:
        return JSONResponse({'authenticated': True}, status_code=200)
    return {"updated": True}
