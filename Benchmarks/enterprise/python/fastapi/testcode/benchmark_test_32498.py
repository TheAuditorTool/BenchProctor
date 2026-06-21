# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from dataclasses import dataclass
from starlette.responses import HTMLResponse


@dataclass
class FormData:
    payload: str

async def BenchmarkTest32498(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = FormData(payload=header_value).payload
    return HTMLResponse('<script src="' + str(data) + '"></script>')
