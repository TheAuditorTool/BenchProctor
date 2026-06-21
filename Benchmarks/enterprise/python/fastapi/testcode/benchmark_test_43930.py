# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest43930(request: Request):
    host_value = request.headers.get('host', '')
    data = host_value if host_value else 'default'
    return JSONResponse({'error': str(data), 'stack': repr(locals())}, status_code=500)
