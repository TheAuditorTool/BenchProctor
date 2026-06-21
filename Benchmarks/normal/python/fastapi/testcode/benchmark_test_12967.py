# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from pydantic import BaseModel
from starlette.responses import HTMLResponse


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest12967(request: Request, req: UserInput):
    json_value = req.payload
    data = json_value if json_value else 'default'
    return HTMLResponse('<html><body><h1>' + str(data) + '</h1></body></html>')
