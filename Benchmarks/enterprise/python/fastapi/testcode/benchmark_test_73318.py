# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from pydantic import BaseModel


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest73318(request: Request, req: UserInput):
    json_value = req.payload
    if json_value:
        data = json_value
    else:
        data = ''
    return JSONResponse({'error': 'An internal error occurred'}, status_code=500)
