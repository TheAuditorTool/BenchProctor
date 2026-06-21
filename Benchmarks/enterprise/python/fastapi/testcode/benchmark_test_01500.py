# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from pydantic import BaseModel
from starlette.responses import HTMLResponse


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest01500(request: Request, req: UserInput):
    json_value = req.payload
    if json_value:
        data = json_value
    else:
        data = ''
    return HTMLResponse('<html><body><h1>' + str(data) + '</h1></body></html>')
