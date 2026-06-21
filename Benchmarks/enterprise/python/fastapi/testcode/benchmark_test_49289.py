# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from app_runtime import auth_check


def default_blank(value):
    return value if value is not None else ''

async def BenchmarkTest49289(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data = default_blank(upload_name)
    if not auth_check(str(data), request.session.get('token')):
        return JSONResponse({'error': 'unauthorized'}, status_code=401)
    return {"updated": True}
