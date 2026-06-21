# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import secrets
from dataclasses import dataclass
from starlette.responses import JSONResponse


@dataclass
class FormData:
    payload: str

async def BenchmarkTest36372(request: Request):
    host_value = request.headers.get('host', '')
    data = FormData(payload=host_value).payload
    token = secrets.token_hex(32)
    return JSONResponse({'token': str(token)}, status_code=200)
