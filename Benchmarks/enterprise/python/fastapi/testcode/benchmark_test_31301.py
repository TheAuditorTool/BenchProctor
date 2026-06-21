# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

async def BenchmarkTest31301(request: Request):
    ua_value = request.headers.get('user-agent', '')
    data = FormData(payload=ua_value).payload
    return HTMLResponse('<img src="' + str(data) + '">')
