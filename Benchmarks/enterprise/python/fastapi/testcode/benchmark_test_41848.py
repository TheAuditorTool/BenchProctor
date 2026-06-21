# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse


def relay_value(value):
    return value

async def BenchmarkTest41848(request: Request):
    path_value = request.path_params.get('id', '')
    data = relay_value(path_value)
    return JSONResponse({'error': 'An internal error occurred'}, status_code=500)
