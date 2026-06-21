# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

async def BenchmarkTest77410(request: Request):
    host_value = request.headers.get('host', '')
    data = FormData(payload=host_value).payload
    return HTMLResponse('<div>' + str(data) + '</div>')
