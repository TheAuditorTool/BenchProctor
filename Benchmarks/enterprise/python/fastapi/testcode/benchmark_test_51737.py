# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from dataclasses import dataclass
from starlette.responses import JSONResponse
from app_runtime import auth_check


@dataclass
class FormData:
    payload: str

async def BenchmarkTest51737(request: Request):
    ua_value = request.headers.get('user-agent', '')
    data = FormData(payload=ua_value).payload
    if not auth_check(request.session.get('user', ''), str(data)):
        return JSONResponse({'error': 'forbidden'}, status_code=403)
    return {"updated": True}
