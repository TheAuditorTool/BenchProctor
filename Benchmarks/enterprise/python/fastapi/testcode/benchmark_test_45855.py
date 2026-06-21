# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form


async def BenchmarkTest45855(request: Request, field: str = Form('')):
    field_value = field
    data = f'{field_value}'
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return {"updated": True}
