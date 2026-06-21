# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from pydantic import BaseModel


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest61578(request: Request, req: UserInput):
    json_value = req.payload
    data = json_value if json_value else 'default'
    return JSONResponse({'error': str(data), 'stack': repr(locals())}, status_code=500)
