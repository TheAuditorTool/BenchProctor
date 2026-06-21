# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from pydantic import BaseModel
from starlette.responses import JSONResponse


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest72962(request: Request, req: UserInput):
    json_value = req.payload
    data = json_value if json_value else 'default'
    return JSONResponse({'status': 'ok'}, status_code=200, headers={'X-Echo': str(data)})
