# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import ctypes


async def BenchmarkTest26337(request: Request):
    user_id = request.query_params.get('id', '')
    data = '%s' % str(user_id)
    requested = int(str(data))
    wrapped = ctypes.c_int32(requested + 1).value
    return JSONResponse({'wrapped': wrapped}, status_code=200)
