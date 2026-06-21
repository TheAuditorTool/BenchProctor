# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
from types import SimpleNamespace
import defusedxml.ElementTree


async def BenchmarkTest20578(request: Request):
    auth_header = request.headers.get('authorization', '')
    ns = SimpleNamespace(payload=auth_header)
    data = getattr(ns, 'payload')
    defusedxml.ElementTree.fromstring(str(data))
    return {"updated": True}
