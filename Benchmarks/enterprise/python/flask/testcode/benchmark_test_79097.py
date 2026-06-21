# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import asyncio
import importlib
import sys


request_state: dict[str, str] = {}

def BenchmarkTest79097():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    request_state['last_input'] = graphql_var
    data = request_state['last_input']
    async def _evasion_task():
        sys.path.insert(0, str(data))
        importlib.import_module('report_renderer')
    asyncio.run(_evasion_task())
    return jsonify({"result": "success"})
