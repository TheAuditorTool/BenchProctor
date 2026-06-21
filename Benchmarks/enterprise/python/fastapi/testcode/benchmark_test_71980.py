# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import secrets
from fastapi import Form
from starlette.responses import JSONResponse
import json


async def BenchmarkTest71980(request: Request, field: str = Form('')):
    field_value = field
    try:
        data = json.loads(field_value).get('value', field_value)
    except (json.JSONDecodeError, AttributeError):
        data = field_value
    token = secrets.token_hex(32)
    return JSONResponse({'token': str(token)}, status_code=200)
