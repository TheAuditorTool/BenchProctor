# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form


async def BenchmarkTest30728(request: Request, field: str = Form('')):
    field_value = field
    data = '{}'.format(field_value)
    try:
        result = int(str(data))
    except Exception:
        pass
    return {"updated": True}
