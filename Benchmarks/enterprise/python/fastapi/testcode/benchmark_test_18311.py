# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
import json
import os
from types import SimpleNamespace


async def BenchmarkTest18311(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    ns = SimpleNamespace(payload=graphql_var)
    data = getattr(ns, 'payload')
    if os.environ.get("APP_ENV", "production") != "test":
        requests.get(str(data))
    return {"updated": True}
