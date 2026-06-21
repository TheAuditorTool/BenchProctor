# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import secrets
from starlette.responses import JSONResponse
import json


async def BenchmarkTest73111(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    try:
        data = json.loads(multipart_value).get('value', multipart_value)
    except (json.JSONDecodeError, AttributeError):
        data = multipart_value
    token = secrets.token_hex(32)
    return JSONResponse({'token': str(token)}, status_code=200)
