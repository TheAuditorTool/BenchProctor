# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import threading
from fastapi import Form


async def BenchmarkTest78039(request: Request, field: str = Form('')):
    field_value = field
    globals()['counter'] = int(field_value)
    return {"updated": True}
