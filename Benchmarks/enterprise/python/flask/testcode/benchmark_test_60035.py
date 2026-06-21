# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import request, jsonify
import asyncio


def BenchmarkTest60035():
    auth_header = request.headers.get('Authorization', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return auth_header
    data = asyncio.run(fetch_payload())
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
