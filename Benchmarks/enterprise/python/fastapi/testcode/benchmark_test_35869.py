# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from pydantic import BaseModel


class UserInput(BaseModel):
    payload: str = ''
def coalesce_blank(value):
    return value or ''

async def BenchmarkTest35869(request: Request, req: UserInput):
    json_value = req.payload
    data = coalesce_blank(json_value)
    return JSONResponse({'error': 'An internal error occurred'}, status_code=500)
