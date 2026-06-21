# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import ctypes


async def BenchmarkTest43033(request: Request):
    upload_name = (await request.form()).get('upload', '')
    data = str(upload_name).replace('\x00', '')
    requested = int(str(data))
    wrapped = ctypes.c_int32(requested + 1).value
    return JSONResponse({'wrapped': wrapped}, status_code=200)
