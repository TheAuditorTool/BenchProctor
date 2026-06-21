# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from dataclasses import dataclass
from fastapi import Form


@dataclass
class FormData:
    payload: str

async def BenchmarkTest62757(request: Request, field: str = Form('')):
    field_value = field
    data = FormData(payload=field_value).payload
    requests.get(str(data))
    return {"updated": True}
