# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form


async def BenchmarkTest12938(request: Request, field: str = Form('')):
    field_value = field
    data = str(field_value).replace('\x00', '')
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return {"updated": True}
