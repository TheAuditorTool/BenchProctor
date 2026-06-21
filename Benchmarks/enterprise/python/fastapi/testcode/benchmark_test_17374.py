# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json
import importlib


async def BenchmarkTest17374(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    data = (lambda v: v.strip())(graphql_var)
    importlib.import_module(str(data))
    return {"updated": True}
