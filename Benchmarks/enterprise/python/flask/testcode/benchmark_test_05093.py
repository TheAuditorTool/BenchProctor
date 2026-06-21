# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify
import asyncio


request_state: dict[str, str] = {}

def BenchmarkTest05093():
    referer_value = request.headers.get('Referer', '')
    request_state['last_input'] = referer_value
    data = request_state['last_input']
    async def _evasion_task():
        os.system('echo ' + str(data))
    asyncio.run(_evasion_task())
    return jsonify({"result": "success"})
