# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


async def BenchmarkTest80496(request: Request):
    path_value = request.path_params.get('id', '')
    return JSONResponse({'error': 'An internal error occurred'}, status_code=500)
