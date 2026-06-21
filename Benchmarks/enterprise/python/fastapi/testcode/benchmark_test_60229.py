# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from starlette.responses import JSONResponse


async def BenchmarkTest60229(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    if env_value:
        data = env_value
    else:
        data = ''
    if str(data) in ('localhost', 'internal-gateway'):
        return JSONResponse({'authenticated': True}, status_code=200)
    return {"updated": True}
