# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
from jinja2 import Environment
from pydantic import BaseModel


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest13125(request: Request, req: UserInput):
    json_value = req.payload
    data = ' '.join(str(json_value).split())
    return HTMLResponse(Environment(autoescape=True).from_string('{{ value }}').render(value=data))
