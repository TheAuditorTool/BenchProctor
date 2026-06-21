# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form


def default_blank(value):
    return value if value is not None else ''

async def BenchmarkTest63713(request: Request, field: str = Form('')):
    field_value = field
    data = default_blank(field_value)
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return {"updated": True}
