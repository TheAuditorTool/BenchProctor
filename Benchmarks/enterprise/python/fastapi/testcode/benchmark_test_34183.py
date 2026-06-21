# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest34183(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    return JSONResponse({'error': str(header_value), 'stack': repr(locals())}, status_code=500)
