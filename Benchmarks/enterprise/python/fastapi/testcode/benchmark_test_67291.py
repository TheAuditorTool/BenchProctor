# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from jinja2 import Template
from starlette.responses import HTMLResponse
from pydantic import BaseModel


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest67291(request: Request, req: UserInput):
    json_value = req.payload
    data = str(json_value).replace('\x00', '')
    return HTMLResponse(Template(data).render())
