# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify
import asyncio


def BenchmarkTest24759():
    referer_value = request.headers.get('Referer', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return referer_value
    data = asyncio.run(fetch_payload())
    session['data'] = str(data)
    return jsonify({"result": "success"})
