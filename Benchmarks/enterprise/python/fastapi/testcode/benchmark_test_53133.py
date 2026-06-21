# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form
from types import SimpleNamespace
import defusedxml.ElementTree


async def BenchmarkTest53133(request: Request, field: str = Form('')):
    field_value = field
    ns = SimpleNamespace(payload=field_value)
    data = getattr(ns, 'payload')
    defusedxml.ElementTree.fromstring(str(data))
    return {"updated": True}
