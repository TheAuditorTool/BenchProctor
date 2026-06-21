# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json
import importlib
import sys


request_state: dict[str, str] = {}

async def BenchmarkTest18982(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    request_state['last_input'] = graphql_var
    data = request_state['last_input']
    eval(compile("sys.path.insert(0, str(data))\nimportlib.import_module('report_renderer')", '<sink>', 'exec'))
    return {"updated": True}
