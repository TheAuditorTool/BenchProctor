# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
from pydantic import BaseModel


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest43645(request: Request, req: UserInput):
    json_value = req.payload
    return HTMLResponse('<div>' + str(json_value) + '</div>')
