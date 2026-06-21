# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import bleach
from dataclasses import dataclass
import os


@dataclass
class FormData:
    payload: str

async def BenchmarkTest18050(request: Request):
    env_value = os.environ.get('USER_INPUT', '')
    data = FormData(payload=env_value).payload
    processed = bleach.clean(data)
    return HTMLResponse('<div>' + str(processed) + '</div>')
