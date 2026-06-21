# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import secrets
from starlette.responses import JSONResponse
import json


async def BenchmarkTest13914(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    try:
        data = json.loads(raw_body).get('value', raw_body)
    except (json.JSONDecodeError, AttributeError):
        data = raw_body
    token = secrets.token_hex(32)
    return JSONResponse({'token': str(token)}, status_code=200)
