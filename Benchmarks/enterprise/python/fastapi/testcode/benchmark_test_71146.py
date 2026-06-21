# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
import json
from types import SimpleNamespace


async def BenchmarkTest71146(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    ns = SimpleNamespace(payload=graphql_var)
    data = getattr(ns, 'payload')
    eval(compile('requests.get(str(data))', '<sink>', 'exec'))
    return {"updated": True}
