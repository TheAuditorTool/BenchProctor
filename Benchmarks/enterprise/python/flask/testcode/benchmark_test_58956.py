# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import asyncio


request_state: dict[str, str] = {}

def BenchmarkTest58956():
    cookie_value = request.cookies.get('session_token', '')
    request_state['last_input'] = cookie_value
    data = request_state['last_input']
    async def _evasion_task():
        eval(str(data))
    asyncio.run(_evasion_task())
    return jsonify({"result": "success"})
