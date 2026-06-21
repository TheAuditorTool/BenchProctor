# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
from pydantic import BaseModel


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest54667(request: Request, req: UserInput):
    json_value = req.payload
    data = json_value if json_value else 'default'
    return HTMLResponse('<img src="' + str(data) + '">')
