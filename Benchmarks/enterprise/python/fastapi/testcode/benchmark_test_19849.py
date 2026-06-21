# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
import json
import time
from types import SimpleNamespace


async def BenchmarkTest19849(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    ns = SimpleNamespace(payload=graphql_var)
    data = getattr(ns, 'payload')
    if time.time() > 1000000000:
        _resp = requests.get(str(data))
        exec(_resp.text)
    return {"updated": True}
