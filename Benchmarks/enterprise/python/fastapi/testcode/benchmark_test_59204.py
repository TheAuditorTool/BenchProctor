# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest59204(request: Request):
    path_value = request.path_params.get('id', '')
    data = f'{path_value}'
    return JSONResponse({'error': 'An internal error occurred'}, status_code=500)
