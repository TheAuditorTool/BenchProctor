# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest69901(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    return JSONResponse({'error': 'An internal error occurred'}, status_code=500)
