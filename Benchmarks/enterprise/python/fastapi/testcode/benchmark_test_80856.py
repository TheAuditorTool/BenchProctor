# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import hashlib
import os
from starlette.responses import JSONResponse


async def BenchmarkTest80856(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data, _sep, _rest = str(env_value).partition('\x00')
    digest = hashlib.sha256(('static_salt_123' + str(data)).encode()).hexdigest()
    return JSONResponse({'digest': str(digest)}, status_code=200)
