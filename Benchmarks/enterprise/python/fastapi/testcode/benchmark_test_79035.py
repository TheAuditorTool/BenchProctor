# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from pydantic import BaseModel
from starlette.responses import HTMLResponse


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest79035(request: Request, req: UserInput):
    json_value = req.payload
    prefix = ''
    data = prefix + str(json_value)
    return HTMLResponse('<html><body><h1>' + str(data) + '</h1></body></html>')
