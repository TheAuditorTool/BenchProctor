# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest62832(request: Request):
    origin_value = request.headers.get('origin', '')
    data = ' '.join(str(origin_value).split())
    if str(data).startswith('https://admin.internal/'):
        return JSONResponse({'authenticated': True}, status_code=200)
    return {"updated": True}
