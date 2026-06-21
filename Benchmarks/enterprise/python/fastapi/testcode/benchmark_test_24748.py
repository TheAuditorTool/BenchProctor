# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import threading
from fastapi import Form


async def BenchmarkTest24748(request: Request, field: str = Form('')):
    field_value = field
    data = field_value if field_value else 'default'
    globals()['counter'] = int(data)
    return {"updated": True}
