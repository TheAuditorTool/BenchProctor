# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from app_runtime import auth_check


async def BenchmarkTest63051(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    if raw_body:
        data = raw_body
    else:
        data = ''
    if not auth_check(str(data), request.session.get('token')):
        return JSONResponse({'error': 'unauthorized'}, status_code=401)
    return {"updated": True}
