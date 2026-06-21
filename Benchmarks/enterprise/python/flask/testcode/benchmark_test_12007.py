# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import request, jsonify
import asyncio


def BenchmarkTest12007():
    referer_value = request.headers.get('Referer', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return referer_value
    data = asyncio.run(fetch_payload())
    digest = hashlib.sha1(str(data).encode()).hexdigest()
    return jsonify({'digest': str(digest)}), 200
