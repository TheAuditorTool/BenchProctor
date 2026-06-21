# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from pydantic import BaseModel


class UserInput(BaseModel):
    payload: str = ''
def default_blank(value):
    return value if value is not None else ''

async def BenchmarkTest01589(request: Request, req: UserInput):
    json_value = req.payload
    data = default_blank(json_value)
    return JSONResponse({'error': 'An internal error occurred'}, status_code=500)
