# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from jinja2 import Template
from starlette.responses import HTMLResponse
from pydantic import BaseModel
import json


class UserInput(BaseModel):
    payload: str = ''

async def BenchmarkTest73164(request: Request, req: UserInput):
    json_value = req.payload
    try:
        data = json.loads(json_value).get('value', json_value)
    except (json.JSONDecodeError, AttributeError):
        data = json_value
    return HTMLResponse(Template(data).render())
