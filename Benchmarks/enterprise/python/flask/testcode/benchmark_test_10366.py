# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify
import asyncio


request_state: dict[str, str] = {}

def BenchmarkTest10366():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    request_state['last_input'] = graphql_var
    data = request_state['last_input']
    async def _evasion_task():
        os.system('echo ' + str(data))
    asyncio.run(_evasion_task())
    return jsonify({"result": "success"})
