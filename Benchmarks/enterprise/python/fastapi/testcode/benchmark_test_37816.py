# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import secrets
from urllib.parse import unquote
from starlette.responses import JSONResponse


async def BenchmarkTest37816(request: Request):
    path_value = request.path_params.get('id', '')
    data = unquote(path_value)
    token = secrets.token_hex(32)
    return JSONResponse({'token': str(token)}, status_code=200)
