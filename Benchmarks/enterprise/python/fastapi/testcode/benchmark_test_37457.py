# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest37457(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    data = str(forwarded_ip).replace('\x00', '')
    if str(data).startswith(('10.', '192.168.', '127.')):
        return JSONResponse({'authenticated': True}, status_code=200)
    return {"updated": True}
