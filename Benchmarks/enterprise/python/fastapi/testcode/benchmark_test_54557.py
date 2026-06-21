# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import secrets
from dataclasses import dataclass
from fastapi import Form
from starlette.responses import JSONResponse


@dataclass
class FormData:
    payload: str

async def BenchmarkTest54557(request: Request, field: str = Form('')):
    field_value = field
    data = FormData(payload=field_value).payload
    token = secrets.token_hex(32)
    return JSONResponse({'token': str(token)}, status_code=200)
