# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest81338(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    allowed = {'https://app.pycdn.io', 'https://admin.pycdn.io'}
    origin = str(header_value)
    if origin in allowed:
        return JSONResponse({'status': 'ok'}, status_code=200, headers={'Access-Control-Allow-Origin': origin})
    return {"updated": True}
