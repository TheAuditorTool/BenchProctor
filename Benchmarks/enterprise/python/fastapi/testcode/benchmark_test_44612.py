# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from pydantic import BaseModel


class UserInput(BaseModel):
    payload: str = ''
def to_text(value):
    return str(value).strip()

async def BenchmarkTest44612(request: Request, req: UserInput):
    json_value = req.payload
    data = to_text(json_value)
    return JSONResponse({'error': 'An internal error occurred'}, status_code=500)
