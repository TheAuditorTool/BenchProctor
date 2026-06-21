# SPDX-License-Identifier: Apache-2.0
from flask import make_response
from flask import request, jsonify
import asyncio


def BenchmarkTest09212():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return forwarded_ip
    data = asyncio.run(fetch_payload())
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(data))
    return resp
