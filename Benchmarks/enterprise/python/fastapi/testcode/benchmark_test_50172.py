# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from app_runtime import auth_check


async def BenchmarkTest50172(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    data = f'{multipart_value:.200s}'
    if auth_check('user', str(data)):
        return JSONResponse({'authenticated': True}, status_code=200)
    return {"updated": True}
