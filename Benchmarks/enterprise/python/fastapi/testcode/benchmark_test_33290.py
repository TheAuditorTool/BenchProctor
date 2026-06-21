# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

async def BenchmarkTest33290(request: Request):
    host_value = request.headers.get('host', '')
    data = FormData(payload=host_value).payload
    request.session['data'] = str(data)
    return {"updated": True}
