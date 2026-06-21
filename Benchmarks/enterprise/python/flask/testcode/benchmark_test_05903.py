# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import asyncio
import importlib


def BenchmarkTest05903():
    header_value = request.headers.get('X-Custom-Header', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return header_value
    data = asyncio.run(fetch_payload())
    if data not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    importlib.import_module(str(processed))
    return jsonify({"result": "success"})
