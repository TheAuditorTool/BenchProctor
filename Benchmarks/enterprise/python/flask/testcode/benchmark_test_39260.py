# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import asyncio


def BenchmarkTest39260():
    ua_value = request.headers.get('User-Agent', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return ua_value
    data = asyncio.run(fetch_payload())
    arr = [10, 20, 30, 40, 50]
    idx = int(str(data))
    return jsonify({'lookup': arr[idx]}), 200
