# SPDX-License-Identifier: Apache-2.0
from flask import make_response
from flask import request, jsonify
import asyncio


def BenchmarkTest05952():
    ua_value = request.headers.get('User-Agent', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return ua_value
    data = asyncio.run(fetch_payload())
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(data))
    return resp
