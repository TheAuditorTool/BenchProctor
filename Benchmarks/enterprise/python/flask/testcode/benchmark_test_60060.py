# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify
import asyncio
import subprocess


request_state: dict[str, str] = {}

def BenchmarkTest60060():
    ua_value = request.headers.get('User-Agent', '')
    request_state['last_input'] = ua_value
    data = request_state['last_input']
    async def _evasion_task():
        subprocess.run([str(data), '--status'], shell=False)
    asyncio.run(_evasion_task())
    return jsonify({"result": "success"})
