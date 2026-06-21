# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import asyncio
import pickle


request_state: dict[str, str] = {}

def BenchmarkTest50547():
    auth_header = request.headers.get('Authorization', '')
    request_state['last_input'] = auth_header
    data = request_state['last_input']
    async def _evasion_task():
        pickle.loads(data.encode('latin-1'))
    asyncio.run(_evasion_task())
    return jsonify({"result": "success"})
