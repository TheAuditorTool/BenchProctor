# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import urllib.request
from types import SimpleNamespace


async def BenchmarkTest45536(request: Request):
    ua_value = request.headers.get('user-agent', '')
    ns = SimpleNamespace(payload=ua_value)
    data = getattr(ns, 'payload')
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(data)).read()
    return {"updated": True}
