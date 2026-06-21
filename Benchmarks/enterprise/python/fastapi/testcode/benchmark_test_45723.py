# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from pydantic import BaseModel
from starlette.responses import HTMLResponse


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest45723(request: Request, req: UserInput):
    json_value = req.payload
    data = str(json_value).replace('\x00', '')
    return HTMLResponse('<html><body><h1>' + str(data) + '</h1></body></html>')
