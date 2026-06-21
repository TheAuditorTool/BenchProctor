# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form


async def BenchmarkTest27800(request: Request, field: str = Form('')):
    field_value = field
    data = ' '.join(str(field_value).split())
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return {"updated": True}
