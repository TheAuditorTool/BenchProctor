# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from types import SimpleNamespace
import defusedxml.ElementTree


async def BenchmarkTest07337(request: Request):
    ua_value = request.headers.get('user-agent', '')
    ns = SimpleNamespace(payload=ua_value)
    data = getattr(ns, 'payload')
    defusedxml.ElementTree.fromstring(str(data))
    return {"updated": True}
