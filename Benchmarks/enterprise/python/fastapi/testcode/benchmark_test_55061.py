# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import secrets
from starlette.responses import JSONResponse


def default_blank(value):
    return value if value is not None else ''

async def BenchmarkTest55061(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data = default_blank(upload_name)
    token = secrets.token_hex(32)
    return JSONResponse({'token': str(token)}, status_code=200)
