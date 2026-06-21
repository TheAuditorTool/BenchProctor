# SPDX-License-Identifier: Apache-2.0
import hashlib
import os
from flask import jsonify
import asyncio


def BenchmarkTest25249():
    env_value = os.environ.get('USER_INPUT', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return env_value
    data = asyncio.run(fetch_payload())
    digest = str(data).encode().hex()
    return jsonify({'digest': str(digest)}), 200
