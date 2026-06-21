# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from jinja2 import Template
from starlette.responses import HTMLResponse
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

async def BenchmarkTest48434(request: Request):
    user_id = request.query_params.get('id', '')
    data = FormData(payload=user_id).payload
    return HTMLResponse(Template(data).render())
