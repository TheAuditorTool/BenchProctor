# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import threading
from fastapi import Form
from types import SimpleNamespace


async def BenchmarkTest75008(request: Request, field: str = Form('')):
    field_value = field
    ns = SimpleNamespace(payload=field_value)
    data = getattr(ns, 'payload')
    globals()['counter'] = int(data)
    return {"updated": True}
