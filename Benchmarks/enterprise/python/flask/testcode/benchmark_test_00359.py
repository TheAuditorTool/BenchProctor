# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
import asyncio


def BenchmarkTest00359(path_param):
    path_value = path_param
    async def fetch_payload():
        await asyncio.sleep(0)
        return path_value
    data = asyncio.run(fetch_payload())
    processed = data[:64]
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(processed)}
