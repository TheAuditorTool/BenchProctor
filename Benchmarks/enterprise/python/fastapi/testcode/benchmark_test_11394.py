# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import html
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

async def BenchmarkTest11394(request: Request):
    user_id = request.query_params.get('id', '')
    data = FormData(payload=user_id).payload
    processed = html.escape(data)
    return HTMLResponse('<div>' + str(processed) + '</div>')
