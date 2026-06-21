# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json
import requests
from types import SimpleNamespace


async def BenchmarkTest31997(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    ns = SimpleNamespace(payload=graphql_var)
    data = getattr(ns, 'payload')
    processed = data[:64]
    requests.get('https://api.pycdn.io/data', params={'q': str(processed)}, verify=False)
    return {"updated": True}
