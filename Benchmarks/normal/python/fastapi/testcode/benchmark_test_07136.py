# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from app_runtime import auth_check


async def BenchmarkTest07136(request: Request):
    upload_name = (await request.form()).get('upload', '')
    if auth_check('user', str(upload_name)):
        return JSONResponse({'authenticated': True}, status_code=200)
    return {"updated": True}
