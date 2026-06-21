# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from fastapi import Form
from types import SimpleNamespace


async def BenchmarkTest81354(request: Request, field: str = Form('')):
    field_value = field
    ns = SimpleNamespace(payload=field_value)
    data = getattr(ns, 'payload')
    size = min(int(data) if str(data).isdigit() else 0, 1024)
    data = bytearray(size)
    return {"updated": True}
