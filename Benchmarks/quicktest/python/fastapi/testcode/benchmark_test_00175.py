# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import threading
from dataclasses import dataclass
from fastapi import Form


@dataclass
class FormData:
    payload: str

async def BenchmarkTest00175(request: Request, field: str = Form('')):
    field_value = field
    data = FormData(payload=field_value).payload
    globals()['counter'] = int(data)
    return {"updated": True}
