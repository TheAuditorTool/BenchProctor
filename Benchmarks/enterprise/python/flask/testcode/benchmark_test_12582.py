# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import asyncio


def BenchmarkTest12582():
    origin_value = request.headers.get('Origin', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return origin_value
    data = asyncio.run(fetch_payload())
    if str(data).startswith('https://admin.internal/'):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
