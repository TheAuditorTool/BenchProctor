# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import ctypes


def to_text(value):
    return str(value).strip()

async def BenchmarkTest06236(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = to_text(header_value)
    requested = int(str(data))
    wrapped = ctypes.c_int32(requested + 1).value
    return JSONResponse({'wrapped': wrapped}, status_code=200)
