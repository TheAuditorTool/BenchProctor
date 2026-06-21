# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest24561(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    if header_value:
        data = header_value
    else:
        data = ''
    if str(data) == 'S3cr3tToken':
        return JSONResponse({'authenticated': True}, status_code=200)
    return {"updated": True}
