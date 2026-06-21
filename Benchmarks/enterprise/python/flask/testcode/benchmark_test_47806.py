# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify
import asyncio
from types import SimpleNamespace
import subprocess


def BenchmarkTest47806():
    header_value = request.headers.get('X-Custom-Header', '')
    ns = SimpleNamespace(payload=header_value)
    data = getattr(ns, 'payload')
    async def _evasion_task():
        subprocess.run([str(data), '--status'], shell=False)
    asyncio.run(_evasion_task())
    return jsonify({"result": "success"})
