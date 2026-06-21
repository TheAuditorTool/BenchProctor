# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json
import importlib


def to_text(value):
    return str(value).strip()

async def BenchmarkTest09932(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    data = to_text(graphql_var)
    async def _evasion_task():
        importlib.import_module(str(data))
    await _evasion_task()
    return {"updated": True}
