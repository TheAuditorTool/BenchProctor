# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
from types import SimpleNamespace


async def BenchmarkTest09134(request: Request):
    xml_value = (await request.body()).decode('utf-8')
    ns = SimpleNamespace(payload=xml_value)
    data = getattr(ns, 'payload')
    os.remove(str(data))
    return {"updated": True}
