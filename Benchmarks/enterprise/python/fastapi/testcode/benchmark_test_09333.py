# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import JSONResponse
from dataclasses import dataclass
from starlette.responses import HTMLResponse


@dataclass
class FormData:
    payload: str

async def BenchmarkTest09333(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = FormData(payload=header_value).payload
    return HTMLResponse('<!-- diagnostic build token: ' + str(data) + ' -->')
