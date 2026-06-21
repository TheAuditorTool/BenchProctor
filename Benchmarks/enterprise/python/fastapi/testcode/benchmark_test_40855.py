# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from dataclasses import dataclass


@dataclass
class FormData:
    payload: str

async def BenchmarkTest40855(request: Request):
    host_value = request.headers.get('host', '')
    data = FormData(payload=host_value).payload
    try:
        result = int(str(data))
    except Exception:
        pass
    return {"updated": True}
