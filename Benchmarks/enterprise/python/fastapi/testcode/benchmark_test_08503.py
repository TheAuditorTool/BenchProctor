# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from dataclasses import dataclass
from fastapi import Form


@dataclass
class FormData:
    payload: str

async def BenchmarkTest08503(request: Request, field: str = Form('')):
    field_value = field
    data = FormData(payload=field_value).payload
    result = 100 / int(str(data))
    return {"updated": True}
