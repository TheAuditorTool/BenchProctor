# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from dataclasses import dataclass
from fastapi import Form
from starlette.responses import JSONResponse
from app_runtime import auth_check


@dataclass
class FormData:
    payload: str

async def BenchmarkTest50979(request: Request, field: str = Form('')):
    field_value = field
    data = FormData(payload=field_value).payload
    if not auth_check(str(data), request.session.get('token')):
        return JSONResponse({'error': 'unauthorized'}, status_code=401)
    return {"updated": True}
