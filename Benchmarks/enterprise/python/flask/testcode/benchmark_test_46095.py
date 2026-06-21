# SPDX-License-Identifier: Apache-2.0
from flask import make_response
import os
from flask import jsonify
import asyncio


def BenchmarkTest46095():
    env_value = os.environ.get('USER_INPUT', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return env_value
    data = asyncio.run(fetch_payload())
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(data))
    return resp
