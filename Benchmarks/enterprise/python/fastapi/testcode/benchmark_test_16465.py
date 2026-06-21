# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from dataclasses import dataclass
from fastapi import Form


@dataclass
class FormData:
    payload: str

async def BenchmarkTest16465(request: Request, field: str = Form('')):
    field_value = field
    data = FormData(payload=field_value).payload
    globals().setdefault('_secret_cache', {})['current'] = str(data)
    return {"updated": True}
