# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from flask import session
import asyncio
from app_runtime import db


def BenchmarkTest36141():
    field_value = request.form.get('field', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return field_value
    data = asyncio.run(fetch_payload())
    if data != session.get('csrf_token'):
        return jsonify({'error': 'CSRF token mismatch'}), 403
    db.execute('UPDATE users SET name = ?', (str(data),))
    return jsonify({"result": "success"})
