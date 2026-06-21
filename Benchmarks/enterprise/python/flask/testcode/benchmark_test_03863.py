# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import jsonify
import asyncio


def BenchmarkTest03863(path_param):
    path_value = path_param
    async def fetch_payload():
        await asyncio.sleep(0)
        return path_value
    data = asyncio.run(fetch_payload())
    digest = hashlib.sha256(str(data).encode()).hexdigest()
    return jsonify({'digest': str(digest)}), 200
