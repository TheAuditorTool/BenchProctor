# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import RedirectResponse
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

async def BenchmarkTest61921(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = FormData(payload=header_value).payload
    return RedirectResponse(url=str(data))
