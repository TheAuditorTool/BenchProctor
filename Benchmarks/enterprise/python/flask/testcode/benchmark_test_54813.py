# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import request, jsonify
import asyncio


def BenchmarkTest54813():
    origin_value = request.headers.get('Origin', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return origin_value
    data = asyncio.run(fetch_payload())
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
