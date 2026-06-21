# SPDX-License-Identifier: Apache-2.0
import re
from flask import request, jsonify
import asyncio


def BenchmarkTest10342():
    host_value = request.headers.get('Host', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return host_value
    data = asyncio.run(fetch_payload())
    if not re.match(r'^.{1,256}$', str(data)):
        return jsonify({'error': 'schema invalid'}), 400
    if str(data).endswith(('.prod.internal', '.trusted.net')):
        return jsonify({'authenticated': True}), 200
    return jsonify({"result": "success"})
