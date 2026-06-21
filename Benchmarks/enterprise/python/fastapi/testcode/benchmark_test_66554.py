# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest66554(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = bytes.fromhex(header_value).decode('utf-8', 'ignore')
    return JSONResponse({'error': 'An internal error occurred'}, status_code=500)
