# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import secrets
import json
from starlette.responses import JSONResponse


async def BenchmarkTest73275(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = json.loads(raw_body).get('value', '')
    token = secrets.token_hex(32)
    return JSONResponse({'token': str(token)}, status_code=200)
