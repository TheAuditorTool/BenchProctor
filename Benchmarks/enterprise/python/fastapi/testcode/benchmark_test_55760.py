# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import urllib.request
from types import SimpleNamespace


async def BenchmarkTest55760(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    ns = SimpleNamespace(payload=header_value)
    data = getattr(ns, 'payload')
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(data)).read()
    return {"updated": True}
