# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from pydantic import BaseModel
from starlette.responses import JSONResponse


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest49283(request: Request, req: UserInput):
    json_value = req.payload
    data = f'{json_value}'
    return JSONResponse({'status': 'ok'}, status_code=200, headers={'X-Echo': str(data)})
