# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from types import SimpleNamespace


async def BenchmarkTest27401(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    ns = SimpleNamespace(payload=xml_value)
    data = getattr(ns, 'payload')
    data = bytearray(int(data) if str(data).isdigit() else 0)
    return {"updated": True}
