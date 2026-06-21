# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form


async def BenchmarkTest12002(request: Request, field: str = Form('')):
    field_value = field
    data = (lambda v: v.strip())(field_value)
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return {"updated": True}
