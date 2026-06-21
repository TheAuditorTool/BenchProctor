# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import hashlib
import os
from starlette.responses import JSONResponse


async def BenchmarkTest35908(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data = env_value if env_value else 'default'
    digest = hashlib.sha1(str(data).encode()).hexdigest()
    return JSONResponse({'digest': str(digest)}, status_code=200)
