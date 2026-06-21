# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from pydantic import BaseModel
import os


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest40194(request: Request, req: UserInput):
    json_value = req.payload
    data = '%s' % str(json_value)
    entries = os.listdir(str(data))
    return JSONResponse({'listing': entries}, status_code=200)
