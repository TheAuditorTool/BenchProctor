# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest12282(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    return JSONResponse({'error': str(forwarded_ip), 'stack': repr(locals())}, status_code=500)
