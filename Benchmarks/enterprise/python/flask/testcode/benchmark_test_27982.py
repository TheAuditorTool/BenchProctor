# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify
import asyncio


def BenchmarkTest27982():
    header_value = request.headers.get('X-Custom-Header', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return header_value
    data = asyncio.run(fetch_payload())
    os.remove(str(data))
    return jsonify({"result": "success"})
