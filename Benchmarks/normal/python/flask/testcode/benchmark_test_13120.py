# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import request, jsonify
import asyncio


def BenchmarkTest13120():
    raw_body = request.get_data(as_text=True)
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(raw_body)
    data = collected
    async def _evasion_task():
        subprocess.run('echo ' + str(data), shell=True)
    asyncio.run(_evasion_task())
    return jsonify({"result": "success"})
