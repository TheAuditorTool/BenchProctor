# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify
import asyncio


def BenchmarkTest06009():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return json_value
    data = asyncio.run(fetch_payload())
    session['data'] = str(data)
    return jsonify({"result": "success"})
