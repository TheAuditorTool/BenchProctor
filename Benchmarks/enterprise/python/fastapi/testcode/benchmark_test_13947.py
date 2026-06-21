# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from starlette.responses import HTMLResponse


async def BenchmarkTest13947(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    if raw_body not in ('asc', 'desc', 'name', 'created'):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = raw_body
    return HTMLResponse(str(processed))
