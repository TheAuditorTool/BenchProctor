# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import bleach
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

async def BenchmarkTest48370(request: Request):
    user_id = request.query_params.get('id', '')
    data = FormData(payload=user_id).payload
    processed = bleach.clean(data)
    return HTMLResponse('<div>' + str(processed) + '</div>')
