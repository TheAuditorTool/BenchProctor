# SPDX-License-Identifier: Apache-2.0
import re
from flask import request, jsonify
import asyncio


def BenchmarkTest44753():
    header_value = request.headers.get('X-Custom-Header', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return header_value
    data = asyncio.run(fetch_payload())
    if not re.fullmatch('^[\\w\\s.\\-:/=\\r\\n]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    return '<html><body><h1>' + str(processed) + '</h1></body></html>', 200, {'Content-Type': 'text/html'}
