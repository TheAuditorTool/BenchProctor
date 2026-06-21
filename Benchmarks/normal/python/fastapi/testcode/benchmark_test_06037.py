# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import secrets
from starlette.responses import JSONResponse


def coalesce_blank(value):
    return value or ''

async def BenchmarkTest06037(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data = coalesce_blank(upload_name)
    token = secrets.token_hex(32)
    return JSONResponse({'token': str(token)}, status_code=200)
