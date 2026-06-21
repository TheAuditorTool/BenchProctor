# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form


async def BenchmarkTest07271(request: Request, field: str = Form('')):
    field_value = field
    data = ' '.join(str(field_value).split())
    int(str(data))
    return {"updated": True}
