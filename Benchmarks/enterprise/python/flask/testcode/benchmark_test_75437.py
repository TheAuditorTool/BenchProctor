# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify
import asyncio


def BenchmarkTest75437():
    cookie_value = request.cookies.get('session_token', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return cookie_value
    data = asyncio.run(fetch_payload())
    session['data'] = str(data)
    return jsonify({"result": "success"})
