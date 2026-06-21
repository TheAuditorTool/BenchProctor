# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from types import SimpleNamespace


async def BenchmarkTest10244(request: Request):
    referer_value = request.headers.get('referer', '')
    ns = SimpleNamespace(payload=referer_value)
    data = getattr(ns, 'payload')
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=False)
    return {"updated": True}
