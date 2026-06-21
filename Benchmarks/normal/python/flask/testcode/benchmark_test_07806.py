# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import request, jsonify
import asyncio


def BenchmarkTest07806():
    header_value = request.headers.get('X-Custom-Header', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return header_value
    data = asyncio.run(fetch_payload())
    eval(compile("subprocess.run('echo ' + str(data), shell=True)", '<sink>', 'exec'))
    return jsonify({"result": "success"})
