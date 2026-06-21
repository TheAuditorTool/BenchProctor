# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import RedirectResponse
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

async def BenchmarkTest58663(request: Request):
    origin_value = request.headers.get('origin', '')
    data = FormData(payload=origin_value).payload
    return RedirectResponse(url=str(data))
