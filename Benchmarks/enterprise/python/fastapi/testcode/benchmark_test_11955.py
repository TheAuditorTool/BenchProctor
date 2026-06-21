# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from dataclasses import dataclass
from starlette.responses import JSONResponse
import ctypes


@dataclass
class FormData:
    payload: str

async def BenchmarkTest11955(request: Request):
    host_value = request.headers.get('host', '')
    data = FormData(payload=host_value).payload
    requested = int(str(data))
    wrapped = ctypes.c_int32(requested + 1).value
    return JSONResponse({'wrapped': wrapped}, status_code=200)
