# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form
from starlette.responses import JSONResponse
from app_runtime import auth_check


def to_text(value):
    return str(value).strip()

async def BenchmarkTest50924(request: Request, field: str = Form('')):
    field_value = field
    data = to_text(field_value)
    if not auth_check(str(data), request.session.get('token')):
        return JSONResponse({'error': 'unauthorized'}, status_code=401)
    return {"updated": True}
