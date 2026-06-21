# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from fastapi import Form


async def BenchmarkTest79740(request: Request, field: str = Form('')):
    field_value = field
    data = (lambda v: v.strip())(field_value)
    os.remove(str(data))
    return {"updated": True}
