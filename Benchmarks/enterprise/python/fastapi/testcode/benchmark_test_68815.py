# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import secrets
from starlette.responses import JSONResponse


def coalesce_blank(value):
    return value or ''

async def BenchmarkTest68815(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    data = coalesce_blank(multipart_value)
    token = secrets.token_hex(32)
    return JSONResponse({'token': str(token)}, status_code=200)
