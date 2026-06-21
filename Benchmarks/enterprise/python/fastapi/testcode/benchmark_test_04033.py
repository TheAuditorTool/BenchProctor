# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from fastapi import Form


async def BenchmarkTest04033(request: Request, field: str = Form('')):
    field_value = field
    def normalize(value):
        return value.strip()
    data = normalize(field_value)
    os.remove(str(data))
    return {"updated": True}
