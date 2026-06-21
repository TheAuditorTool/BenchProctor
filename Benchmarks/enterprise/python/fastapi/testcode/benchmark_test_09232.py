# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import os


async def BenchmarkTest09232(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data = str(env_value).replace('\x00', '')
    return JSONResponse({'error': str(data), 'stack': repr(locals())}, status_code=500)
