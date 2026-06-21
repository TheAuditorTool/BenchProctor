# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
import time
from types import SimpleNamespace


async def BenchmarkTest00413(request: Request):
    referer_value = request.headers.get('referer', '')
    ns = SimpleNamespace(payload=referer_value)
    data = getattr(ns, 'payload')
    if time.time() > 1000000000:
        requests.get(str(data))
    return {"updated": True}
