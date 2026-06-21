# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from dataclasses import dataclass
from fastapi import Form


@dataclass
class FormData:
    payload: str

async def BenchmarkTest08772(request: Request, field: str = Form('')):
    field_value = field
    data = FormData(payload=field_value).payload
    os.remove(str(data))
    return {"updated": True}
