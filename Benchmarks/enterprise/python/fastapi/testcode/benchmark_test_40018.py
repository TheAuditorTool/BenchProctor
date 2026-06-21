# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


def relay_value(value):
    return value

async def BenchmarkTest40018(request: Request):
    origin_value = request.headers.get('origin', '')
    data = relay_value(origin_value)
    return JSONResponse({'status': 'ok'}, status_code=200, headers={'X-Echo': str(data)})
