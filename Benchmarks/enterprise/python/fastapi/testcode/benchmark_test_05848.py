# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from starlette.responses import JSONResponse
from app_runtime import auth_check


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest05848(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    reader = make_reader(env_value)
    data = reader()
    if not auth_check(str(data), request.session.get('token')):
        return JSONResponse({'error': 'unauthorized'}, status_code=401)
    return {"updated": True}
