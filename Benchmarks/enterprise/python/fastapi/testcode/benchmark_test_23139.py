# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from pydantic import BaseModel
from starlette.responses import HTMLResponse


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest23139(request: Request, req: UserInput):
    json_value = req.payload
    kind = 'json' if str(json_value).lstrip().startswith('{') else 'text'
    match kind:
        case 'json':
            parsed = json_value
            data = parsed
        case _:
            data = json_value
    return HTMLResponse('<!-- diagnostic build token: ' + str(data) + ' -->')
