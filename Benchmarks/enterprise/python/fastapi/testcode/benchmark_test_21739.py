# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest21739(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    data = '{}'.format(forwarded_ip)
    if str(data) == 'is_admin':
        return JSONResponse({'access': 'granted', 'role': 'admin'}, status_code=200)
    return {"updated": True}
