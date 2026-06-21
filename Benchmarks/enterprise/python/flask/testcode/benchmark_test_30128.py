# SPDX-License-Identifier: Apache-2.0
import jwt
from flask import jsonify
import asyncio


def BenchmarkTest30128():
    secret_value = 'config_secret_test_abc123'
    async def fetch_payload():
        await asyncio.sleep(0)
        return secret_value
    data = asyncio.run(fetch_payload())
    jwt.encode({'sub': 'user'}, data, algorithm='HS256')
    return jsonify({"result": "success"})
