# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form


async def BenchmarkTest74948(request: Request, field: str = Form('')):
    field_value = field
    data = ' '.join(str(field_value).split())
    try:
        result = int(str(data))
    except Exception:
        pass
    return {"updated": True}
