# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import asyncio


def BenchmarkTest78570():
    xml_value = request.get_data(as_text=True)
    async def fetch_payload():
        await asyncio.sleep(0)
        return xml_value
    data = asyncio.run(fetch_payload())
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(data)}
