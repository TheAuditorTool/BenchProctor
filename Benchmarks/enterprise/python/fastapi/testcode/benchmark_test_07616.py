# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import urllib.request
from types import SimpleNamespace


async def BenchmarkTest07616(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    ns = SimpleNamespace(payload=forwarded_ip)
    data = getattr(ns, 'payload')
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(data)).read()
    return {"updated": True}
