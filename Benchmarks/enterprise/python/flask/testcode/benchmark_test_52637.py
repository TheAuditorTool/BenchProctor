# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import request, jsonify
import asyncio
from types import SimpleNamespace


def BenchmarkTest52637():
    upload_name = request.files['upload'].filename
    ns = SimpleNamespace(payload=upload_name)
    data = getattr(ns, 'payload')
    async def _evasion_task():
        subprocess.run('echo ' + str(data), shell=True)
    asyncio.run(_evasion_task())
    return jsonify({"result": "success"})
