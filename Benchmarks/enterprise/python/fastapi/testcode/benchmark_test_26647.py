# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
import ctypes


async def BenchmarkTest26647(request: Request):
    user_id = request.query_params.get('id', '')
    requested = int(str(user_id))
    wrapped = ctypes.c_int32(requested + 1).value
    return JSONResponse({'wrapped': wrapped}, status_code=200)
