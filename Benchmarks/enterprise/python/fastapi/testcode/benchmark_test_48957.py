# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json
import importlib


def ensure_str(value):
    return str(value)

async def BenchmarkTest48957(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    data = ensure_str(graphql_var)
    async def _evasion_task():
        importlib.import_module(str(data))
    await _evasion_task()
    return {"updated": True}
