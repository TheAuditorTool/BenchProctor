# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from app_runtime import auth_check


async def BenchmarkTest67454(request: Request):
    upload_name = (await request.form()).get('upload', '')
    if not auth_check(request.session.get('user', ''), str(upload_name)):
        return JSONResponse({'error': 'forbidden'}, status_code=403)
    return {"updated": True}
