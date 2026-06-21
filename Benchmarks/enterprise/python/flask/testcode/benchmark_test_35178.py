# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import request, jsonify
import asyncio


def BenchmarkTest35178():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return forwarded_ip
    data = asyncio.run(fetch_payload())
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
