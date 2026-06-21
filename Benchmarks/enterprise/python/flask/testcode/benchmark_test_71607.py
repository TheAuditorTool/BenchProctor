# SPDX-License-Identifier: Apache-2.0
from flask import make_response
from flask import request, jsonify
import asyncio


def BenchmarkTest71607():
    auth_header = request.headers.get('Authorization', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return auth_header
    data = asyncio.run(fetch_payload())
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(data), max_age=86400)
    return resp
