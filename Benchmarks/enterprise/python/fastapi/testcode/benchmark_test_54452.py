# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from fastapi import Form
from types import SimpleNamespace


async def BenchmarkTest54452(request: Request, field: str = Form('')):
    field_value = field
    ns = SimpleNamespace(payload=field_value)
    data = getattr(ns, 'payload')
    os.remove(str(data))
    return {"updated": True}
