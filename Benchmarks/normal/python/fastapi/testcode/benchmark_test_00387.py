# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import ctypes


def ensure_str(value):
    return str(value)

async def BenchmarkTest00387(request: Request):
    path_value = request.path_params.get('id', '')
    data = ensure_str(path_value)
    processed = data[:64]
    requested = int(str(processed))
    wrapped = ctypes.c_int32(requested + 1).value
    return JSONResponse({'wrapped': wrapped}, status_code=200)
