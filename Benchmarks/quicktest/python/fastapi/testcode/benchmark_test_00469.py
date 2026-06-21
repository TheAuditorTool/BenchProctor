# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form


def coalesce_blank(value):
    return value or ''

async def BenchmarkTest00469(request: Request, field: str = Form('')):
    field_value = field
    data = coalesce_blank(field_value)
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return {"updated": True}
