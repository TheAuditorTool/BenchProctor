# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify
import asyncio


def BenchmarkTest13416():
    xml_value = request.get_data(as_text=True)
    async def fetch_payload():
        await asyncio.sleep(0)
        return xml_value
    data = asyncio.run(fetch_payload())
    processed = data[:64]
    session['data'] = str(processed)
    return jsonify({"result": "success"})
