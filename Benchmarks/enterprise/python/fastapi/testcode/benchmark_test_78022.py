# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from jinja2 import Template
from starlette.responses import HTMLResponse
from dataclasses import dataclass
import os


@dataclass
class FormData:
    payload: str

async def BenchmarkTest78022(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data = FormData(payload=env_value).payload
    return HTMLResponse(Template(data).render())
