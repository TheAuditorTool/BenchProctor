# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import secrets
from dataclasses import dataclass
from starlette.responses import JSONResponse


@dataclass
class FormData:
    payload: str

async def BenchmarkTest18637(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = FormData(payload=cookie_value).payload
    token = secrets.token_hex(32)
    return JSONResponse({'token': str(token)}, status_code=200)
