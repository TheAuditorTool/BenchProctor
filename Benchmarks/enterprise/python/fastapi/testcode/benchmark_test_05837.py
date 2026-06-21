# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json
from types import SimpleNamespace
from app_runtime import auth_check


async def BenchmarkTest05837(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    ns = SimpleNamespace(payload=graphql_var)
    data = getattr(ns, 'payload')
    auth_check('user', data)
    return {"updated": True}
