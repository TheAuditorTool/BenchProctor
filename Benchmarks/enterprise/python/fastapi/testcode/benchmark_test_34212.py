# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import html
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

async def BenchmarkTest34212(request: Request):
    origin_value = request.headers.get('origin', '')
    data = FormData(payload=origin_value).payload
    processed = html.escape(data)
    return HTMLResponse('<div>' + str(processed) + '</div>')
