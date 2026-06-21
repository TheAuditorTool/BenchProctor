# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify
import asyncio
import subprocess


def BenchmarkTest01734():
    auth_header = request.headers.get('Authorization', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(auth_header)
    data = collected
    async def _evasion_task():
        subprocess.run([str(data), '--status'], shell=False)
    asyncio.run(_evasion_task())
    return jsonify({"result": "success"})
