# SPDX-License-Identifier: Apache-2.0
import jwt
import os
from flask import jsonify
import asyncio


def BenchmarkTest01652():
    secret_value = 'feature_flag_value'
    async def fetch_payload():
        await asyncio.sleep(0)
        return secret_value
    data = asyncio.run(fetch_payload())
    store_cred = os.environ.get('APP_SECRET', '')
    jwt.encode({'sub': str(data)}, store_cred, algorithm='HS256')
    return jsonify({"result": "success"})
