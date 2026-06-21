# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json
import importlib
from types import SimpleNamespace


async def BenchmarkTest75939(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    ns = SimpleNamespace(payload=graphql_var)
    data = getattr(ns, 'payload')
    eval(compile('importlib.import_module(str(data))', '<sink>', 'exec'))
    return {"updated": True}
