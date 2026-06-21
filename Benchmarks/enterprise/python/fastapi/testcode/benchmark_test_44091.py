# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from dataclasses import dataclass
from starlette.responses import RedirectResponse
import urllib.parse


@dataclass
class FormData:
    payload: str

async def BenchmarkTest44091(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    data = FormData(payload=forwarded_ip).payload
    target = '/dashboard?hidden_field=' + urllib.parse.quote(str(data))
    return RedirectResponse(url=target)
