# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
from flask import request
import asyncio


request_state: dict[str, str] = {}

def BenchmarkTest08861():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    request_state['last_input'] = graphql_var
    data = request_state['last_input']
    async def _evasion_task():
        return render_template_string(data)
    return asyncio.run(_evasion_task())
