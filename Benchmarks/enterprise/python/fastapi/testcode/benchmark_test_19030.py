# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from pydantic import BaseModel


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest19030(request: Request, req: UserInput):
    json_value = req.payload
    return JSONResponse({'error': str(json_value), 'stack': repr(locals())}, status_code=500)
