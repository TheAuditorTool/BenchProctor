# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from fastapi import Form
from types import SimpleNamespace


async def BenchmarkTest52953(request: Request, field: str = Form('')):
    field_value = field
    ns = SimpleNamespace(payload=field_value)
    data = getattr(ns, 'payload')
    base_name = os.path.basename(str(data))
    os.chmod('/var/app/data/' + base_name, 0o600)
    return {"updated": True}
