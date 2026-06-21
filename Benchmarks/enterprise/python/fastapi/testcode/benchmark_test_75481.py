# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from pydantic import BaseModel
import os


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest75481(request: Request, req: UserInput):
    json_value = req.payload
    data = str(json_value).replace('\x00', '')
    entries = os.listdir(str(data))
    return JSONResponse({'listing': entries}, status_code=200)
