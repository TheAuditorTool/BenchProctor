# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import html
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

async def BenchmarkTest07584(request: Request):
    referer_value = request.headers.get('referer', '')
    data = FormData(payload=referer_value).payload
    processed = html.escape(data)
    return HTMLResponse('<div>' + str(processed) + '</div>')
