# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest56169(request: Request):
    host_value = request.headers.get('host', '')
    return JSONResponse({'error': str(host_value), 'stack': repr(locals())}, status_code=500)
