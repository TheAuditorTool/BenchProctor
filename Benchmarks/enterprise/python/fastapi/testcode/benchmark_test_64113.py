# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from jinja2 import Template
from starlette.responses import HTMLResponse
from dataclasses import dataclass
from pydantic import BaseModel


class UserInput(BaseModel):
    payload: str = ''
@dataclass
class FormData:
    payload: str

async def BenchmarkTest64113(request: Request, req: UserInput):
    json_value = req.payload
    data = FormData(payload=json_value).payload
    return HTMLResponse(Template(data).render())
