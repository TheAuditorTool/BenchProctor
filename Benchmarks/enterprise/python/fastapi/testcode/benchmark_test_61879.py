# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest61879(request: Request):
    referer_value = request.headers.get('referer', '')
    allowed = {'https://app.pycdn.io', 'https://admin.pycdn.io'}
    origin = str(referer_value)
    if origin in allowed:
        return JSONResponse({'status': 'ok'}, status_code=200, headers={'Access-Control-Allow-Origin': origin})
    return {"updated": True}
