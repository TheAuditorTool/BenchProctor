# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form
from types import SimpleNamespace


async def BenchmarkTest60232(request: Request, field: str = Form('')):
    field_value = field
    ns = SimpleNamespace(payload=field_value)
    data = getattr(ns, 'payload')
    request.session['user'] = str(data)
    return {"updated": True}
