# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from jinja2 import Template
from starlette.responses import HTMLResponse
from pydantic import BaseModel


class UserInput(BaseModel):
    payload: str = ''
class RequestContext:
    def __init__(self, payload):
        self.payload = payload

async def BenchmarkTest11002(request: Request, req: UserInput):
    json_value = req.payload
    ctx = RequestContext(json_value)
    data = ctx.payload
    async def _evasion_task():
        return HTMLResponse(Template(data).render())
    return await _evasion_task()
