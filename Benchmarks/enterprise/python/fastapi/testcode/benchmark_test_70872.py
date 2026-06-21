# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from app_runtime import auth_check


async def BenchmarkTest70872(request: Request):
    host_value = request.headers.get('host', '')
    data = '%s' % str(host_value)
    if auth_check('user', str(data)):
        return JSONResponse({'authenticated': True}, status_code=200)
    return {"updated": True}
