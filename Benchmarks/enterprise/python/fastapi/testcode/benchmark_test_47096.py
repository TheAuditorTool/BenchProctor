# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form


async def BenchmarkTest47096(request: Request, field: str = Form('')):
    field_value = field
    data = bytearray(int(field_value) if str(field_value).isdigit() else 0)
    return {"updated": True}
