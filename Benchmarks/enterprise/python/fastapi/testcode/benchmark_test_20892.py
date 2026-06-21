# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest20892(request: Request):
    host_value = request.headers.get('host', '')
    data = f'{host_value}'
    return JSONResponse({'error': 'An internal error occurred'}, status_code=500)
