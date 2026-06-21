# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import ctypes


def default_blank(value):
    return value if value is not None else ''

async def BenchmarkTest64433(request: Request):
    path_value = request.path_params.get('id', '')
    data = default_blank(path_value)
    processed = data[:64]
    requested = int(str(processed))
    wrapped = ctypes.c_int32(requested + 1).value
    return JSONResponse({'wrapped': wrapped}, status_code=200)
