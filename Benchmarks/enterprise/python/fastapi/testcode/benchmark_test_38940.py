# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from jinja2 import Template
from starlette.responses import HTMLResponse
from jinja2 import Environment
from pydantic import BaseModel


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest38940(request: Request, req: UserInput):
    json_value = req.payload
    return HTMLResponse(Environment(autoescape=True).from_string('safe block: {{ value }}').render(value=json_value))
