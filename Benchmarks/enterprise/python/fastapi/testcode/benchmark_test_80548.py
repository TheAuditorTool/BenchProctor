# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest80548(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    prefix = ''
    data = prefix + str(forwarded_ip)
    values = str(data).split(',')
    if values:
        return JSONResponse({'first': values[0], 'dropped': len(values) - 1}, status_code=200)
    return {"updated": True}
