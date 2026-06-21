# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form


def relay_value(value):
    return value

async def BenchmarkTest22786(request: Request, field: str = Form('')):
    field_value = field
    data = relay_value(field_value)
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return {"updated": True}
