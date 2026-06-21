# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from starlette.responses import JSONResponse
import ctypes


def default_blank(value):
    return value if value is not None else ''

async def BenchmarkTest45989(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data = default_blank(env_value)
    processed = data[:64]
    requested = int(str(processed))
    wrapped = ctypes.c_int32(requested + 1).value
    return JSONResponse({'wrapped': wrapped}, status_code=200)
