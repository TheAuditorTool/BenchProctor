# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from jinja2 import Template
from starlette.responses import HTMLResponse
import os


async def BenchmarkTest01767(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data = env_value if env_value else 'default'
    return HTMLResponse(Template(data).render())
