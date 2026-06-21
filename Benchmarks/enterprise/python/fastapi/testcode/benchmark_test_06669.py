# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import html
from dataclasses import dataclass
import os


@dataclass
class FormData:
    payload: str

async def BenchmarkTest06669(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data = FormData(payload=env_value).payload
    processed = html.escape(data)
    return HTMLResponse('<div>' + str(processed) + '</div>')
