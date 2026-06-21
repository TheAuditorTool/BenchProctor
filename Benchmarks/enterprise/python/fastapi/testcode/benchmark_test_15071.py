# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from dataclasses import dataclass
from fastapi import Form
import json


@dataclass
class FormData:
    payload: str

async def BenchmarkTest15071(request: Request, field: str = Form('')):
    field_value = field
    data = FormData(payload=field_value).payload
    json.loads(data)
    return {"updated": True}
