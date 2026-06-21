# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from flask import session
import asyncio
from app_runtime import auth_check


def BenchmarkTest17761():
    upload_name = request.files['upload'].filename
    async def fetch_payload():
        await asyncio.sleep(0)
        return upload_name
    data = asyncio.run(fetch_payload())
    if not auth_check(session.get('user', ''), str(data)):
        return jsonify({'error': 'forbidden'}), 403
    return jsonify({"result": "success"})
