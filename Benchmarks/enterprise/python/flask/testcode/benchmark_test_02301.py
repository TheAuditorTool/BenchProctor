# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from flask import session
import asyncio
from app_runtime import auth_check


def BenchmarkTest02301():
    auth_header = request.headers.get('Authorization', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return auth_header
    data = asyncio.run(fetch_payload())
    if not auth_check(session.get('user', ''), str(data)):
        return jsonify({'error': 'forbidden'}), 403
    return jsonify({"result": "success"})
