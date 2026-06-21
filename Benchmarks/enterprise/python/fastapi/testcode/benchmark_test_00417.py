# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from pydantic import BaseModel


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest00417(request: Request, req: UserInput):
    json_value = req.payload
    data = ' '.join(str(json_value).split())
    return JSONResponse({'error': str(data), 'stack': repr(locals())}, status_code=500)
