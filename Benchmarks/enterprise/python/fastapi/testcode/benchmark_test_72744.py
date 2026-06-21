# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
from pydantic import BaseModel


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest72744(request: Request, req: UserInput):
    json_value = req.payload
    data = ' '.join(str(json_value).split())
    return HTMLResponse('<div>' + str(data) + '</div>')
