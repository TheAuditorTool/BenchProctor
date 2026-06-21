# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form


async def BenchmarkTest10994(request: Request, field: str = Form('')):
    field_value = field
    data = f'{field_value:.200s}'
    try:
        result = int(str(data))
    except Exception:
        pass
    return {"updated": True}
