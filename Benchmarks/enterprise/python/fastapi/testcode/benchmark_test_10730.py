# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import bleach
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

async def BenchmarkTest10730(request: Request):
    host_value = request.headers.get('host', '')
    data = FormData(payload=host_value).payload
    processed = bleach.clean(data)
    return HTMLResponse('<div>' + str(processed) + '</div>')
