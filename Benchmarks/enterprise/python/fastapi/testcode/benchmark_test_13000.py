# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import secrets
from starlette.responses import JSONResponse


async def BenchmarkTest13000(request: Request):
    path_value = request.path_params.get('id', '')
    data = '{}'.format(path_value)
    token = secrets.token_hex(32)
    return JSONResponse({'token': str(token)}, status_code=200)
