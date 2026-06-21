# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from pydantic import BaseModel
from starlette.responses import HTMLResponse


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest71111(request: Request, req: UserInput):
    json_value = req.payload
    data, _sep, _rest = str(json_value).partition('\x00')
    return HTMLResponse('<!-- diagnostic build token: ' + str(data) + ' -->')
