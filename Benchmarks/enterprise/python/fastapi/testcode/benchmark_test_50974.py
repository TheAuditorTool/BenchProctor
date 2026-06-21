# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form


async def BenchmarkTest50974(request: Request, field: str = Form('')):
    field_value = field
    size = min(int(field_value) if str(field_value).isdigit() else 0, 1024)
    data = bytearray(size)
    return {"updated": True}
