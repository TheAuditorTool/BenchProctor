# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify
import asyncio
import subprocess


def BenchmarkTest21917():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return forwarded_ip
    data = asyncio.run(fetch_payload())
    async def _evasion_task():
        subprocess.run([str(data), '--status'], shell=False)
    asyncio.run(_evasion_task())
    return jsonify({"result": "success"})
