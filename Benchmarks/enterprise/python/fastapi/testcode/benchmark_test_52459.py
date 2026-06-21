# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from app_runtime import auth_check


async def BenchmarkTest52459(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    if not auth_check(request.session.get('user', ''), str(raw_body)):
        return JSONResponse({'error': 'forbidden'}, status_code=403)
    return {"updated": True}
