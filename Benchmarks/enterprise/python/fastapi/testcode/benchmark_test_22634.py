# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import secrets
from urllib.parse import unquote
from starlette.responses import JSONResponse


async def BenchmarkTest22634(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    data = unquote(multipart_value)
    token = secrets.token_hex(32)
    return JSONResponse({'token': str(token)}, status_code=200)
