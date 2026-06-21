# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import RedirectResponse
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

async def BenchmarkTest51580(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    data = FormData(payload=forwarded_ip).payload
    return RedirectResponse(url=str(data))
