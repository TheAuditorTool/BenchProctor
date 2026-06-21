# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import secrets
from starlette.responses import JSONResponse


def to_text(value):
    return str(value).strip()

async def BenchmarkTest75818(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    data = to_text(multipart_value)
    token = secrets.token_hex(32)
    return JSONResponse({'token': str(token)}, status_code=200)
