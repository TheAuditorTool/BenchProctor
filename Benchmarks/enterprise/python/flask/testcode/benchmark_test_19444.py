# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import request, jsonify
import asyncio


def BenchmarkTest19444():
    raw_body = request.get_data(as_text=True)
    async def fetch_payload():
        await asyncio.sleep(0)
        return raw_body
    data = asyncio.run(fetch_payload())
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
