# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest13462(request: Request):
    auth_header = request.headers.get('authorization', '')
    allowed = {'https://app.pycdn.io', 'https://admin.pycdn.io'}
    origin = str(auth_header)
    if origin in allowed:
        return JSONResponse({'status': 'ok'}, status_code=200, headers={'Access-Control-Allow-Origin': origin})
    return {"updated": True}
