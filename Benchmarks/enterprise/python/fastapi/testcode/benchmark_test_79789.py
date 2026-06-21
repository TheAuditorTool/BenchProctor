# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from fastapi import Form
from types import SimpleNamespace


async def BenchmarkTest79789(request: Request, field: str = Form('')):
    field_value = field
    ns = SimpleNamespace(payload=field_value)
    data = getattr(ns, 'payload')
    try:
        os.setuid(int(str(data)) if str(data).isdigit() else 65534)
    except OSError:
        pass
    return {"updated": True}
