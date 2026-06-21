# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from app_runtime import auth_check


def to_text(value):
    return str(value).strip()

async def BenchmarkTest15956(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data = to_text(upload_name)
    if not auth_check(str(data), request.session.get('token')):
        return JSONResponse({'error': 'unauthorized'}, status_code=401)
    return {"updated": True}
