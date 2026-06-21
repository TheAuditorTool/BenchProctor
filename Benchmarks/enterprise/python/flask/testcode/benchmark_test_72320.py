# SPDX-License-Identifier: Apache-2.0
from flask import make_response
import re
from flask import request, jsonify
import asyncio


def BenchmarkTest72320():
    raw_body = request.get_data(as_text=True)
    async def fetch_payload():
        await asyncio.sleep(0)
        return raw_body
    data = asyncio.run(fetch_payload())
    if not re.fullmatch('^[\\w\\s.,;:_/\\-=]+$', data):
        return jsonify({'error': 'forbidden'}), 400
    processed = data
    resp = make_response(jsonify({'status': 'ok'}))
    resp.set_cookie('session', str(processed), max_age=86400)
    return resp
