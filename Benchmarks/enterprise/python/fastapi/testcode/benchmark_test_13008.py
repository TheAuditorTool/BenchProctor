# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from app_runtime import auth_check


async def BenchmarkTest13008(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    if auth_check('user', str(multipart_value)):
        return JSONResponse({'authenticated': True}, status_code=200)
    return {"updated": True}
