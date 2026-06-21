# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
from flask import session
import asyncio
from app_runtime import auth_check


def BenchmarkTest80686():
    multipart_value = request.form.get('multipart_field', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return multipart_value
    data = asyncio.run(fetch_payload())
    if not auth_check(str(data), session.get('token')):
        return jsonify({'error': 'unauthorized'}), 401
    return jsonify({"result": "success"})
