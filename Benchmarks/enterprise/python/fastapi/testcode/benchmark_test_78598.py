# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form


async def BenchmarkTest78598(request: Request, field: str = Form('')):
    field_value = field
    data = (lambda v: v.strip())(field_value)
    try:
        result = int(str(data))
    except Exception:
        pass
    return {"updated": True}
