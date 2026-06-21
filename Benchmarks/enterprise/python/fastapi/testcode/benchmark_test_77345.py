# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import secrets
from starlette.responses import JSONResponse


async def BenchmarkTest77345(request: Request):
    path_value = request.path_params.get('id', '')
    token = secrets.token_hex(32)
    return JSONResponse({'token': str(token)}, status_code=200)
