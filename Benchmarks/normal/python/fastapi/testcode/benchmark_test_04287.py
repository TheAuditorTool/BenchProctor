# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from pydantic import BaseModel
from starlette.responses import JSONResponse
import ctypes


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest04287(request: Request, req: UserInput):
    json_value = req.payload
    data = '%s' % str(json_value)
    requested = int(str(data))
    wrapped = ctypes.c_int32(requested + 1).value
    return JSONResponse({'wrapped': wrapped}, status_code=200)
