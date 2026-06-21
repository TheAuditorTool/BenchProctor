# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from pydantic import BaseModel


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest60903(request: Request, req: UserInput):
    json_value = req.payload
    prefix = ''
    data = prefix + str(json_value)
    return JSONResponse({'error': str(data), 'stack': repr(locals())}, status_code=500)
