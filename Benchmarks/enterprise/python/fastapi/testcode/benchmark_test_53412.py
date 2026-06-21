# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import secrets
from urllib.parse import unquote
from starlette.responses import JSONResponse


async def BenchmarkTest53412(request: Request):
    user_id = request.query_params.get('id', '')
    data = unquote(user_id)
    token = secrets.token_hex(32)
    return JSONResponse({'token': str(token)}, status_code=200)
