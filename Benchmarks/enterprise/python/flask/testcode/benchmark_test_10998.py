# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import asyncio
from app_runtime import db


def BenchmarkTest10998():
    origin_value = request.headers.get('Origin', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return origin_value
    data = asyncio.run(fetch_payload())
    processed = data[:64]
    record = db.fetch_one('SELECT * FROM documents WHERE id = ?', (str(processed),))
    return jsonify({'record': str(record)}), 200
