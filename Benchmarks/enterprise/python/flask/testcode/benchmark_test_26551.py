# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
import os
from flask import jsonify
import asyncio


def BenchmarkTest26551():
    env_value = os.environ.get('USER_INPUT', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return env_value
    data = asyncio.run(fetch_payload())
    if data not in ('asc', 'desc', 'name', 'created'):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    return render_template_string(processed)
