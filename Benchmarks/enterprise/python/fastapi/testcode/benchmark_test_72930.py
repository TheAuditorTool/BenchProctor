# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from fastapi import Form
from types import SimpleNamespace


async def BenchmarkTest72930(request: Request, field: str = Form('')):
    field_value = field
    ns = SimpleNamespace(payload=field_value)
    data = getattr(ns, 'payload')
    os.setuid(int(str(data)) if str(data).isdigit() else 0)
    return {"updated": True}
