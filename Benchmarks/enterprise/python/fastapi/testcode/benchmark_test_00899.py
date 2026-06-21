# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from jinja2 import Template
from starlette.responses import HTMLResponse


async def BenchmarkTest00899(request: Request):
    user_id = request.query_params.get('id', '')
    data = '{}'.format(user_id)
    return HTMLResponse(Template(data).render())
