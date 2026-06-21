# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

async def BenchmarkTest65292(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    data = FormData(payload=cookie_value).payload
    return HTMLResponse('<div>' + str(data) + '</div>')
