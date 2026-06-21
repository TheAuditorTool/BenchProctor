# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import asyncio


def BenchmarkTest39911():
    ua_value = request.headers.get('User-Agent', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return ua_value
    data = asyncio.run(fetch_payload())
    if not str(data).isdigit():
        raise Exception('error: ' + str(data))
    return jsonify({"result": "success"})
