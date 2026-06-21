# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from types import SimpleNamespace
import defusedxml.ElementTree


async def BenchmarkTest65629(request: Request):
    cookie_value = request.cookies.get('session_token', '')
    ns = SimpleNamespace(payload=cookie_value)
    data = getattr(ns, 'payload')
    defusedxml.ElementTree.fromstring(str(data))
    return {"updated": True}
