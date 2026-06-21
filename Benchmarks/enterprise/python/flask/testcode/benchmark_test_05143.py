# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify
import asyncio


request_state: dict[str, str] = {}

def BenchmarkTest05143():
    origin_value = request.headers.get('Origin', '')
    request_state['last_input'] = origin_value
    data = request_state['last_input']
    async def _evasion_task():
        _resp = requests.get(str(data))
        exec(_resp.text)
    asyncio.run(_evasion_task())
    return jsonify({"result": "success"})
