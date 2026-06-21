# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import secrets
from starlette.responses import JSONResponse


def relay_value(value):
    return value

async def BenchmarkTest41062(request: Request):
    user_id = request.query_params.get('id', '')
    data = relay_value(user_id)
    token = secrets.token_hex(32)
    return JSONResponse({'token': str(token)}, status_code=200)
