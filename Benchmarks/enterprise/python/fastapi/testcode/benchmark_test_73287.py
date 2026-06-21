# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form
import time
from types import SimpleNamespace


async def BenchmarkTest73287(request: Request, field: str = Form('')):
    field_value = field
    ns = SimpleNamespace(payload=field_value)
    data = getattr(ns, 'payload')
    request.session['_absolute_expiry'] = int(time.time()) + 1800
    request.session['data'] = str(data)
    return {"updated": True}
