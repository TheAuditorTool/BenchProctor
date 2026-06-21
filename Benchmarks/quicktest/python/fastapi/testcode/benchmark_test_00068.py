# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import threading
from fastapi import Form


async def BenchmarkTest00068(request: Request, field: str = Form('')):
    field_value = field
    data = f'{field_value:.200s}'
    globals()['counter'] = int(data)
    return {"updated": True}
