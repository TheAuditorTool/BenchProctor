# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import json
from types import SimpleNamespace


async def BenchmarkTest22386(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    ns = SimpleNamespace(payload=graphql_var)
    data = getattr(ns, 'payload')
    os.remove(str(data))
    return {"updated": True}
