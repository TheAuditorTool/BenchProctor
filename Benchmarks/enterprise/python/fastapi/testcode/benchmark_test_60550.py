# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from fastapi import Form


async def BenchmarkTest60550(request: Request, field: str = Form('')):
    field_value = field
    data = field_value if field_value else 'default'
    os.seteuid(65534)
    return {"updated": True}
