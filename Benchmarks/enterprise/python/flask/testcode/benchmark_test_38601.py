# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import asyncio


def BenchmarkTest38601():
    referer_value = request.headers.get('Referer', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return referer_value
    data = asyncio.run(fetch_payload())
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(data)}
