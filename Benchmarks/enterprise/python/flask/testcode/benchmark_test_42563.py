# SPDX-License-Identifier: Apache-2.0
import requests
import os
from flask import jsonify
import asyncio


def BenchmarkTest42563():
    env_value = os.environ.get('USER_INPUT', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return env_value
    data = asyncio.run(fetch_payload())
    processed = data[:64]
    requests.post('http://api.prod.internal/data', data=str(processed))
    return jsonify({"result": "success"})
