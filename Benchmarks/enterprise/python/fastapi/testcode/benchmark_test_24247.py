# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form


async def BenchmarkTest24247(request: Request, field: str = Form('')):
    field_value = field
    data = str(field_value).replace('\x00', '')
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return {"updated": True}
