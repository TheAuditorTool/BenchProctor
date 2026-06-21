# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import threading
from fastapi import Form


async def BenchmarkTest09024(request: Request, field: str = Form('')):
    field_value = field
    data = (lambda v: v.strip())(field_value)
    globals()['counter'] = int(data)
    return {"updated": True}
