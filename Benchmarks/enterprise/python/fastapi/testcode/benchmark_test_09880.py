# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from types import SimpleNamespace
import defusedxml.ElementTree


async def BenchmarkTest09880(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    ns = SimpleNamespace(payload=raw_body)
    data = getattr(ns, 'payload')
    defusedxml.ElementTree.fromstring(str(data))
    return {"updated": True}
