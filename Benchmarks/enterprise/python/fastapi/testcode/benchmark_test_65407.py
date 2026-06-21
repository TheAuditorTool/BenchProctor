# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json
from types import SimpleNamespace


async def BenchmarkTest65407(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    ns = SimpleNamespace(payload=graphql_var)
    data = getattr(ns, 'payload')
    try:
        result = int(str(data))
    except Exception:
        pass
    return {"updated": True}
