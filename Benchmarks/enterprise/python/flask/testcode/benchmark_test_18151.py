# SPDX-License-Identifier: Apache-2.0
from flask import jsonify
from flask import session
import asyncio
from app_runtime import auth_check


def BenchmarkTest18151(path_param):
    path_value = path_param
    async def fetch_payload():
        await asyncio.sleep(0)
        return path_value
    data = asyncio.run(fetch_payload())
    if not auth_check(session.get('user', ''), str(data)):
        return jsonify({'error': 'forbidden'}), 403
    return jsonify({"result": "success"})
