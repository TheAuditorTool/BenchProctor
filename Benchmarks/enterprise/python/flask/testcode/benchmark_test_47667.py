# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
import asyncio
import importlib


request_state: dict[str, str] = {}

def BenchmarkTest47667():
    env_value = os.environ.get('USER_INPUT', '')
    request_state['last_input'] = env_value
    data = request_state['last_input']
    async def _evasion_task():
        importlib.import_module(str(data))
    asyncio.run(_evasion_task())
    return jsonify({"result": "success"})
