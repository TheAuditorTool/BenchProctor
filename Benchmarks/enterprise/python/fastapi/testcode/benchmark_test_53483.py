# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import ctypes


def default_blank(value):
    return value if value is not None else ''

async def BenchmarkTest53483(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = default_blank(header_value)
    requested = int(str(data))
    wrapped = ctypes.c_int32(requested + 1).value
    return JSONResponse({'wrapped': wrapped}, status_code=200)
