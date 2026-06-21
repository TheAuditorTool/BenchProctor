# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from app_runtime import auth_check


async def BenchmarkTest11772(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    def normalize(value):
        return value.strip()
    data = normalize(raw_body)
    if auth_check('user', str(data)):
        return JSONResponse({'authenticated': True}, status_code=200)
    return {"updated": True}
