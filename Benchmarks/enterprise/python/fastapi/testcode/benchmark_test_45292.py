# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from fastapi import Form


def relay_value(value):
    return value

async def BenchmarkTest45292(request: Request, field: str = Form('')):
    field_value = field
    data = relay_value(field_value)
    os.remove(str(data))
    return {"updated": True}
