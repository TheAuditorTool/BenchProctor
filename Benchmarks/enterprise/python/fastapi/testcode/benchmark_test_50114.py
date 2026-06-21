# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form


def to_text(value):
    return str(value).strip()

async def BenchmarkTest50114(request: Request, field: str = Form('')):
    field_value = field
    data = to_text(field_value)
    try:
        result = int(str(data))
    except Exception:
        pass
    return {"updated": True}
