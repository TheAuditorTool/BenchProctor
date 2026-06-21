# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import asyncio


def BenchmarkTest40705():
    cookie_value = request.cookies.get('session_token', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return cookie_value
    data = asyncio.run(fetch_payload())
    return jsonify({'error': 'An internal error occurred'}), 500
