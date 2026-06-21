# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form
from starlette.responses import JSONResponse
import ctypes


async def BenchmarkTest58444(request: Request, field: str = Form('')):
    field_value = field
    data = (lambda v: v.strip())(field_value)
    requested = int(str(data))
    wrapped = ctypes.c_int32(requested + 1).value
    return JSONResponse({'wrapped': wrapped}, status_code=200)
