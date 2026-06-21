# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import html
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

async def BenchmarkTest04599(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    data = FormData(payload=forwarded_ip).payload
    processed = html.escape(data)
    return HTMLResponse('<div>' + str(processed) + '</div>')
