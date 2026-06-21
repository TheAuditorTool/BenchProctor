# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import secrets
from starlette.responses import JSONResponse


def relay_value(value):
    return value

async def BenchmarkTest63964(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    data = relay_value(multipart_value)
    token = secrets.token_hex(32)
    return JSONResponse({'token': str(token)}, status_code=200)
