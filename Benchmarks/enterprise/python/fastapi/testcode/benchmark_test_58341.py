# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import secrets
from dataclasses import dataclass
from starlette.responses import JSONResponse


@dataclass
class FormData:
    payload: str

async def BenchmarkTest58341(request: Request):
    user_id = request.query_params.get('id', '')
    data = FormData(payload=user_id).payload
    token = secrets.token_hex(32)
    return JSONResponse({'token': str(token)}, status_code=200)
