# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import asyncio


def BenchmarkTest80443():
    raw_body = request.get_data(as_text=True)
    async def fetch_payload():
        await asyncio.sleep(0)
        return raw_body
    data = asyncio.run(fetch_payload())
    if str(data) == 'S3cr3tToken':
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
