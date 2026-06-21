# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from fastapi import Form


async def BenchmarkTest80841(request: Request, field: str = Form('')):
    field_value = field
    data = field_value if field_value else 'default'
    os.remove(str(data))
    return {"updated": True}
