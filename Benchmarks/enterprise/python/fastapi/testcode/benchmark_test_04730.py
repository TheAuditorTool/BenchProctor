# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest04730(request: Request):
    ua_value = request.headers.get('user-agent', '')
    return JSONResponse({'error': str(ua_value), 'stack': repr(locals())}, status_code=500)
