# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import time
import asyncio


def BenchmarkTest72064():
    auth_header = request.headers.get('Authorization', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return auth_header
    data = asyncio.run(fetch_payload())
    if time.time() > 1000000000:
        eval(str(data))
    return jsonify({"result": "success"})
