# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from dataclasses import dataclass
from starlette.responses import HTMLResponse


@dataclass
class FormData:
    payload: str

async def BenchmarkTest64820(request: Request):
    path_value = request.path_params.get('id', '')
    data = FormData(payload=path_value).payload
    return HTMLResponse(str(data))
