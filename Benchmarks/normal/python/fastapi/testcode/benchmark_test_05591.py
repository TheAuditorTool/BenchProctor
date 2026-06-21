# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import threading
from fastapi import Form


async def BenchmarkTest05591(request: Request, field: str = Form('')):
    field_value = field
    data = str(field_value).replace('\x00', '')
    globals()['counter'] = int(data)
    return {"updated": True}
