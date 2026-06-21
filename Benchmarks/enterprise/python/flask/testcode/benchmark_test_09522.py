# SPDX-License-Identifier: Apache-2.0
import os
from flask import jsonify
import asyncio


def BenchmarkTest09522():
    env_value = os.environ.get('USER_INPUT', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return env_value
    data = asyncio.run(fetch_payload())
    return jsonify({'error': str(data), 'stack': repr(locals())}), 500
