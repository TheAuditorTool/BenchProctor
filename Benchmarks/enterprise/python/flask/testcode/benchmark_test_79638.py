# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import request, jsonify
import asyncio


def BenchmarkTest79638():
    raw_body = request.get_data(as_text=True)
    async def fetch_payload():
        await asyncio.sleep(0)
        return raw_body
    data = asyncio.run(fetch_payload())
    digest = hashlib.sha256(str(data).encode()).hexdigest()
    return jsonify({'digest': str(digest)}), 200
