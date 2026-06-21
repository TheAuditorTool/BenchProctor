# SPDX-License-Identifier: Apache-2.0
import secrets
from flask import jsonify
import asyncio


def BenchmarkTest20160(path_param):
    path_value = path_param
    async def fetch_payload():
        await asyncio.sleep(0)
        return path_value
    data = asyncio.run(fetch_payload())
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
