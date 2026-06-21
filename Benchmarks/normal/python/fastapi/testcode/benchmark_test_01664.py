# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form


def to_text(value):
    return str(value).strip()

async def BenchmarkTest01664(request: Request, field: str = Form('')):
    field_value = field
    data = to_text(field_value)
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return {"updated": True}
