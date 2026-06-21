# SPDX-License-Identifier: Apache-2.0
import os
import subprocess
from flask import request, jsonify
import asyncio


def BenchmarkTest50162():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return json_value
    data = asyncio.run(fetch_payload())
    subprocess.run(['echo', data], shell=False)
    return jsonify({"result": "success"})
