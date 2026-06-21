# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import secrets
from starlette.responses import JSONResponse


def to_text(value):
    return str(value).strip()

async def BenchmarkTest23108(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    data = to_text(xml_value)
    token = secrets.token_hex(32)
    return JSONResponse({'token': str(token)}, status_code=200)
