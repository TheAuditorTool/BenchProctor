# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from pydantic import BaseModel
from starlette.responses import HTMLResponse


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest35913(request: Request, req: UserInput):
    json_value = req.payload
    return HTMLResponse('<!-- diagnostic build token: ' + str(json_value) + ' -->')
