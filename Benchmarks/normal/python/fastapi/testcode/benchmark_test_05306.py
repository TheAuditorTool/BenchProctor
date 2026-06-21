# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from fastapi import Form


def to_text(value):
    return str(value).strip()

async def BenchmarkTest05306(request: Request, field: str = Form('')):
    field_value = field
    data = to_text(field_value)
    os.remove(str(data))
    return {"updated": True}
