# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from types import SimpleNamespace


async def BenchmarkTest06505(request: Request):
    user_id = request.query_params.get('id', '')
    ns = SimpleNamespace(payload=user_id)
    data = getattr(ns, 'payload')
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=False)
    return {"updated": True}
