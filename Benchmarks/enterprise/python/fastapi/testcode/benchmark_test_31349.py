# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from app_runtime import auth_check


def make_reader(raw):
    def read():
        return raw.strip()
    return read

async def BenchmarkTest31349(request: Request):
    referer_value = request.headers.get('referer', '')
    reader = make_reader(referer_value)
    data = reader()
    if auth_check('user', str(data)):
        return JSONResponse({'authenticated': True}, status_code=200)
    return {"updated": True}
