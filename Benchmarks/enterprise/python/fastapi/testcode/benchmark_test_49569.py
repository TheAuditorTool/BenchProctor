# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest49569(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    parts = str(raw_body).split(',')
    data = ','.join(parts)
    if str(data) in ('admin', 'true', 'authenticated'):
        return JSONResponse({'authenticated': True}, status_code=200)
    return {"updated": True}
