# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


def relay_value(value):
    return value

async def BenchmarkTest79636(request: Request):
    ua_value = request.headers.get('user-agent', '')
    data = relay_value(ua_value)
    processed = data[:64]
    if str(processed) in ('read', 'write', 'delete', 'admin'):
        return JSONResponse({'access': 'granted', 'role': 'admin'}, status_code=200)
    return {"updated": True}
