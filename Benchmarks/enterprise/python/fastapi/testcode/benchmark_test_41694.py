# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import HTMLResponse
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

async def BenchmarkTest41694(request: Request):
    path_value = request.path_params.get('id', '')
    data = FormData(payload=path_value).payload
    return HTMLResponse('<img src="' + str(data) + '">')
