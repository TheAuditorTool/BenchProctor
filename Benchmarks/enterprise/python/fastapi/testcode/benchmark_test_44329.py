# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from starlette.responses import JSONResponse


async def BenchmarkTest44329(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    trusted_claim = str(env_value)
    return JSONResponse({'trusted': trusted_claim}, status_code=200)
