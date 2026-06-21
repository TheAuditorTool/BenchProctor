# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json
from fastapi import Form


def to_text(value):
    return str(value).strip()

async def BenchmarkTest44732(request: Request, field: str = Form('')):
    field_value = field
    data = to_text(field_value)
    json.loads(data)
    return {"updated": True}
