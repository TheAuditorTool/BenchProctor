# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import secrets
from starlette.responses import JSONResponse


def to_text(value):
    return str(value).strip()

async def BenchmarkTest11840(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = to_text(raw_body)
    token = secrets.token_hex(32)
    return JSONResponse({'token': str(token)}, status_code=200)
