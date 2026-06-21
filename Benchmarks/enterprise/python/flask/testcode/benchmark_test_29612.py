# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify
import asyncio


def BenchmarkTest29612():
    host_value = request.headers.get('Host', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return host_value
    data = asyncio.run(fetch_payload())
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return jsonify({"result": "success"})
