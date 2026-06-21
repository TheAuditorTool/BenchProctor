# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json
import urllib.request
from types import SimpleNamespace


async def BenchmarkTest10042(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    ns = SimpleNamespace(payload=graphql_var)
    data = getattr(ns, 'payload')
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(data)).read()
    return {"updated": True}
