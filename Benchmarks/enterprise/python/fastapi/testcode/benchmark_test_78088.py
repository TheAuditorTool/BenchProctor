# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import os


async def BenchmarkTest78088(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    return JSONResponse({'error': 'An internal error occurred'}, status_code=500)
