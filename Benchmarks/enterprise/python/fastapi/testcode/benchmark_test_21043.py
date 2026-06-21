# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from fastapi import Form


def coalesce_blank(value):
    return value or ''

async def BenchmarkTest21043(request: Request, field: str = Form('')):
    field_value = field
    data = coalesce_blank(field_value)
    os.remove(str(data))
    return {"updated": True}
