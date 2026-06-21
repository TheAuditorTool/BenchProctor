# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import jsonify
import asyncio
from app_runtime import auth_check


def BenchmarkTest56616(path_param):
    path_value = path_param
    async def fetch_payload():
        await asyncio.sleep(0)
        return path_value
    data = asyncio.run(fetch_payload())
    if not auth_check('user', hashlib.sha256(str(data).encode()).hexdigest()):
        return jsonify({'error': 'unauthorized'}), 401
    return jsonify({"result": "success"})
