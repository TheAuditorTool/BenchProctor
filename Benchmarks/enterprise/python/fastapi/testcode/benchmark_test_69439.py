# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from dataclasses import dataclass
import os
from starlette.responses import HTMLResponse


@dataclass
class FormData:
    payload: str

async def BenchmarkTest69439(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data = FormData(payload=env_value).payload
    return HTMLResponse('<html><body><h1>' + str(data) + '</h1></body></html>')
