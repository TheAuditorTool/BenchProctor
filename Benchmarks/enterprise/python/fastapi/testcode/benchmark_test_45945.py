# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from pydantic import BaseModel


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest45945(request: Request, req: UserInput):
    json_value = req.payload
    parts = str(json_value).split(',')
    data = ','.join(parts)
    return JSONResponse({'error': 'An internal error occurred'}, status_code=500)
