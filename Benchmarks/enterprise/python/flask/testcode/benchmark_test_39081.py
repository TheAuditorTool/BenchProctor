# SPDX-License-Identifier: Apache-2.0
from flask import make_response
from flask import request, jsonify
import asyncio


def BenchmarkTest39081():
    user_id = request.args.get('id', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return user_id
    data = asyncio.run(fetch_payload())
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(data))
    return resp
