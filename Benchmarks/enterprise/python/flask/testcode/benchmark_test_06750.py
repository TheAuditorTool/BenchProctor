# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import asyncio
from app_runtime import db


def BenchmarkTest06750():
    auth_header = request.headers.get('Authorization', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return auth_header
    data = asyncio.run(fetch_payload())
    record = db.fetch_one('SELECT * FROM documents WHERE id = ?', (str(data),))
    return jsonify({'record': str(record)}), 200
