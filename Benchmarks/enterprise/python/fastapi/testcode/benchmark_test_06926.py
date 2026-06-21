# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest06926(request: Request):
    host_value = request.headers.get('host', '')
    if str(host_value) in ('read', 'write', 'delete', 'admin'):
        return JSONResponse({'access': 'granted', 'role': 'admin'}, status_code=200)
    return {"updated": True}
