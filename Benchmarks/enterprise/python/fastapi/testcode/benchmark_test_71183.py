# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import json
import importlib
import sys


request_state: dict[str, str] = {}

async def BenchmarkTest71183(request: Request):
    graphql_var = json.loads((await request.body()).decode()).get('variables', {}).get('input', '')
    request_state['last_input'] = graphql_var
    data = request_state['last_input']
    async def _evasion_task():
        sys.path.insert(0, str(data))
        importlib.import_module('report_renderer')
    await _evasion_task()
    return {"updated": True}
