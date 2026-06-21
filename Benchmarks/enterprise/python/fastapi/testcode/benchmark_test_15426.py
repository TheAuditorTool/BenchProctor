# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest15426(request: Request):
    origin_value = request.headers.get('origin', '')
    data = f'{origin_value}'
    if str(data) in ('admin', 'true', 'authenticated'):
        return JSONResponse({'authenticated': True}, status_code=200)
    return {"updated": True}
