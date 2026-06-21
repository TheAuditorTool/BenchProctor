# SPDX-License-Identifier: Apache-2.0
from flask import redirect
import re
import os
from flask import jsonify
import asyncio


def BenchmarkTest47652():
    env_value = os.environ.get('USER_INPUT', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return env_value
    data = asyncio.run(fetch_payload())
    if not re.match(r'^.{1,256}$', str(data)):
        return jsonify({'error': 'schema invalid'}), 400
    return redirect(str(data))
