# SPDX-License-Identifier: Apache-2.0
import html
import os
from flask import jsonify
import asyncio


def BenchmarkTest39886():
    env_value = os.environ.get('USER_INPUT', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return env_value
    data = asyncio.run(fetch_payload())
    processed = str(data).replace("<script", "")
    return jsonify({'status': 'ok'}), 200, {'Content-Language': str(processed)}
