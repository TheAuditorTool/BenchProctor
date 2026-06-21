# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import os


async def BenchmarkTest48771(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    return JSONResponse({'error': str(env_value), 'stack': repr(locals())}, status_code=500)
