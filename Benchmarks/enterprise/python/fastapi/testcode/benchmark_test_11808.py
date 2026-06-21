# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import html
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

async def BenchmarkTest11808(request: Request):
    ua_value = request.headers.get('user-agent', '')
    data = FormData(payload=ua_value).payload
    processed = html.escape(data)
    return HTMLResponse('<div>' + str(processed) + '</div>')
