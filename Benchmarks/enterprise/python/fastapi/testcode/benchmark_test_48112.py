# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import re
from starlette.responses import JSONResponse


def relay_value(value):
    return value

async def BenchmarkTest48112(request: Request):
    host_value = request.headers.get('host', '')
    data = relay_value(host_value)
    if not re.match(r'^.{1,256}$', str(data)):
        return JSONResponse({'error': 'schema invalid'}, status_code=400)
    if str(data).endswith(('.prod.internal', '.trusted.net')):
        return JSONResponse({'authenticated': True}, status_code=200)
    return {"updated": True}
