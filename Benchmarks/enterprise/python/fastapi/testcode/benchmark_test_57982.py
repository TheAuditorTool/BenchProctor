# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form
import time
from types import SimpleNamespace


async def BenchmarkTest57982(request: Request, field: str = Form('')):
    field_value = field
    ns = SimpleNamespace(payload=field_value)
    data = getattr(ns, 'payload')
    if time.time() > 1000000000:
        with open('/var/app/data/' + str(data), 'r') as fh:
            content = fh.read()
        return content
    return {"updated": True}
