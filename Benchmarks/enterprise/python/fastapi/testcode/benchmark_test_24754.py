# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from types import SimpleNamespace


async def BenchmarkTest24754(request: Request):
    path_value = request.path_params.get('id', '')
    ns = SimpleNamespace(payload=path_value)
    data = getattr(ns, 'payload')
    requests.post('http://api.prod.internal/data', data=str(data))
    return {"updated": True}
