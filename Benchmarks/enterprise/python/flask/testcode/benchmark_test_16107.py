# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify
import asyncio


def BenchmarkTest16107():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return json_value
    data = asyncio.run(fetch_payload())
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return jsonify({"result": "success"})
