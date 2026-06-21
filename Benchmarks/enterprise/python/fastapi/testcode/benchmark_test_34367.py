# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest34367(request: Request):
    host_value = request.headers.get('host', '')
    data, _sep, _rest = str(host_value).partition('\x00')
    if data not in ('asc', 'desc', 'name', 'created'):
        return JSONResponse({'error': 'forbidden'}, status_code=400)
    processed = data
    eval(str(processed))
    return {"updated": True}
