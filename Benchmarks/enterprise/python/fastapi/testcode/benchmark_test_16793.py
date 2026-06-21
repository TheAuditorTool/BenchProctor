# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form


async def BenchmarkTest16793(request: Request, field: str = Form('')):
    field_value = field
    data = field_value if field_value else 'default'
    try:
        result = int(str(data))
    except Exception:
        pass
    return {"updated": True}
