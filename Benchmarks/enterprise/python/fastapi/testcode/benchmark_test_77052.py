# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import hashlib
import os
from starlette.responses import JSONResponse


async def BenchmarkTest77052(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data = f'{env_value}'
    digest = str(data).encode().hex()
    return JSONResponse({'digest': str(digest)}, status_code=200)
