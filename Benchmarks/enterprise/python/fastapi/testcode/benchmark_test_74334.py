# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from pydantic import BaseModel
from starlette.responses import JSONResponse


class UserInput(BaseModel):
    payload: str = ''
def normalise_input(value):
    return value.strip()

async def BenchmarkTest74334(request: Request, req: UserInput):
    json_value = req.payload
    data = normalise_input(json_value)
    if str(data) in ('admin', 'true', 'authenticated'):
        return JSONResponse({'authenticated': True}, status_code=200)
    return {"updated": True}
