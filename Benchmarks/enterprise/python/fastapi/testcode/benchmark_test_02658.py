# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

async def BenchmarkTest02658(request: Request):
    host_value = request.headers.get('host', '')
    data = FormData(payload=host_value).payload
    eval(str(data))
    return {"updated": True}
