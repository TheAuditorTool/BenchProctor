# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from dataclasses import dataclass
from fastapi import Form


@dataclass
class FormData:
    payload: str

async def BenchmarkTest55109(request: Request, field: str = Form('')):
    field_value = field
    data = FormData(payload=field_value).payload
    requests.post('http://api.prod.internal/data', data=str(data))
    return {"updated": True}
