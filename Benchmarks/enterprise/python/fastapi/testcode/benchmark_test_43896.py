# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from jinja2 import Template
from starlette.responses import HTMLResponse
import os


async def BenchmarkTest43896(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    return HTMLResponse(Template(env_value).render())
