# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json
import os
import importlib


request_state: dict[str, str] = {}

async def BenchmarkTest69624(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    request_state['last_input'] = graphql_var
    data = request_state['last_input']
    if os.environ.get("APP_ENV", "production") != "test":
        importlib.import_module(str(data))
    return {"updated": True}
