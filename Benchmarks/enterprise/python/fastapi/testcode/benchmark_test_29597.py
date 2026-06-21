# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import secrets
from starlette.responses import JSONResponse


async def BenchmarkTest29597(request: Request):
    path_value = request.path_params.get('id', '')
    data = f'{path_value:.200s}'
    token = secrets.token_hex(32)
    return JSONResponse({'token': str(token)}, status_code=200)
