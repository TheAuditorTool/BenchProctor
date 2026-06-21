# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
import html
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

async def BenchmarkTest80525(request: Request):
    path_value = request.path_params.get('id', '')
    data = FormData(payload=path_value).payload
    processed = html.escape(data)
    return HTMLResponse('<img src="' + str(processed) + '">')
