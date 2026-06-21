# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import bleach
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

async def BenchmarkTest02672(request: Request):
    path_value = request.path_params.get('id', '')
    data = FormData(payload=path_value).payload
    processed = bleach.clean(data)
    return HTMLResponse('<div>' + str(processed) + '</div>')
