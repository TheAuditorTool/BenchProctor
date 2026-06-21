# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from app_runtime import auth_check


def normalise_input(value):
    return value.strip()

async def BenchmarkTest11640(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = normalise_input(auth_header)
    if auth_check('user', str(data)):
        return JSONResponse({'authenticated': True}, status_code=200)
    return {"updated": True}
