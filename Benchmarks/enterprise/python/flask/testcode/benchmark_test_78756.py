# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import asyncio


def BenchmarkTest78756():
    header_value = request.headers.get('X-Custom-Header', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return header_value
    data = asyncio.run(fetch_payload())
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return jsonify({"result": "success"})
