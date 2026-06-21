# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form


async def BenchmarkTest45652(request: Request, field: str = Form('')):
    field_value = field
    data = (lambda v: v.strip())(field_value)
    eval(str(data))
    return {"updated": True}
