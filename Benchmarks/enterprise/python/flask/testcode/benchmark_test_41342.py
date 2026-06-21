# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import asyncio
import requests


def BenchmarkTest41342():
    header_value = request.headers.get('X-Custom-Header', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return header_value
    data = asyncio.run(fetch_payload())
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=False)
    return jsonify({"result": "success"})
