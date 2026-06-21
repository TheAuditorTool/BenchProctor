# SPDX-License-Identifier: Apache-2.0
from flask import session
from flask import request, jsonify
import asyncio


def BenchmarkTest08996():
    upload_name = request.files['upload'].filename
    async def fetch_payload():
        await asyncio.sleep(0)
        return upload_name
    data = asyncio.run(fetch_payload())
    session['data'] = str(data)
    return jsonify({"result": "success"})
