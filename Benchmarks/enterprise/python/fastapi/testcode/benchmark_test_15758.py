# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from jinja2 import Template
from starlette.responses import HTMLResponse
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

async def BenchmarkTest15758(request: Request):
    ua_value = request.headers.get('user-agent', '')
    data = FormData(payload=ua_value).payload
    return HTMLResponse(Template(data).render())
