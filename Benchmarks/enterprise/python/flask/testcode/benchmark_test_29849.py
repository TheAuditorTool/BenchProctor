# SPDX-License-Identifier: Apache-2.0
import subprocess
from flask import request, jsonify
import asyncio


def BenchmarkTest29849():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return json_value
    data = asyncio.run(fetch_payload())
    processed = data[:64]
    subprocess.run('echo ' + str(processed), shell=True)
    return jsonify({"result": "success"})
