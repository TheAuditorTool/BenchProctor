# SPDX-License-Identifier: Apache-2.0
import re
from flask import request, jsonify
import asyncio
from app_runtime import db


def BenchmarkTest60174():
    ua_value = request.headers.get('User-Agent', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return ua_value
    data = asyncio.run(fetch_payload())
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    db.execute('DELETE FROM accounts WHERE id = ?', (str(processed),))
    return jsonify({"result": "success"})
