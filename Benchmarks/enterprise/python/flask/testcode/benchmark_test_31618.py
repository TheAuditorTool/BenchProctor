# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import asyncio


def BenchmarkTest31618():
    host_value = request.headers.get('Host', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return host_value
    data = asyncio.run(fetch_payload())
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
