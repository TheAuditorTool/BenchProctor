# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import asyncio


def BenchmarkTest30369():
    field_value = request.form.get('field', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return field_value
    data = asyncio.run(fetch_payload())
    return jsonify({'status': 'ok'}), 200, {'X-Frame-Options': 'DENY', 'Content-Security-Policy': "frame-ancestors 'none'"}
