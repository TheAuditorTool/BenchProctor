# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify
import asyncio


request_state: dict[str, str] = {}

def BenchmarkTest59267():
    host_value = request.headers.get('Host', '')
    request_state['last_input'] = host_value
    data = request_state['last_input']
    async def _evasion_task():
        requests.get(str(data))
    asyncio.run(_evasion_task())
    return jsonify({"result": "success"})
