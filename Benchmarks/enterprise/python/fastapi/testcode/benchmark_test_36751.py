# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from starlette.responses import JSONResponse
import ctypes


async def BenchmarkTest36751(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data = env_value if env_value else 'default'
    requested = int(str(data))
    wrapped = ctypes.c_int32(requested + 1).value
    return JSONResponse({'wrapped': wrapped}, status_code=200)
