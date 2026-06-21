# SPDX-License-Identifier: Apache-2.0
import secrets
import os
from flask import jsonify
import asyncio


def BenchmarkTest67983():
    env_value = os.environ.get('USER_INPUT', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return env_value
    data = asyncio.run(fetch_payload())
    token = secrets.token_hex(32)
    return jsonify({'token': str(token)}), 200
