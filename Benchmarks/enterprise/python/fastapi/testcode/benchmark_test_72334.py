# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import os


async def BenchmarkTest72334(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data = f'{env_value}'
    entries = os.listdir(str(data))
    return JSONResponse({'listing': entries}, status_code=200)
