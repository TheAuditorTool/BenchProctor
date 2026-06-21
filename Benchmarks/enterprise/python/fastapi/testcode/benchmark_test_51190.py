# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest51190(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = ' '.join(str(raw_body).split())
    if str(data) in ('admin', 'true', 'authenticated'):
        return JSONResponse({'authenticated': True}, status_code=200)
    return {"updated": True}
