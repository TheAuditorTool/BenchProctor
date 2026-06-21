# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from starlette.responses import JSONResponse
import ctypes
from types import SimpleNamespace


async def BenchmarkTest71979(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    ns = SimpleNamespace(payload=env_value)
    data = getattr(ns, 'payload')
    requested = int(str(data))
    wrapped = ctypes.c_int32(requested + 1).value
    return JSONResponse({'wrapped': wrapped}, status_code=200)
