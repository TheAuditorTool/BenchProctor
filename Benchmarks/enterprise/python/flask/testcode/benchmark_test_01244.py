# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import request, jsonify
import asyncio


def BenchmarkTest01244():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(json_value)
    data = collected
    async def _evasion_task():
        subprocess.run('echo ' + str(data), shell=True)
    asyncio.run(_evasion_task())
    return jsonify({"result": "success"})
