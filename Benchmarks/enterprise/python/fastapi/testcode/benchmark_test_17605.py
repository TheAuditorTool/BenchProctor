# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from starlette.responses import RedirectResponse
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

async def BenchmarkTest17605(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = FormData(payload=raw_body).payload
    return RedirectResponse(url=str(data))
