# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import asyncio


def BenchmarkTest08643():
    auth_header = request.headers.get('Authorization', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return auth_header
    data = asyncio.run(fetch_payload())
    if str(data).endswith(('/public', '/static', '/.')):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
