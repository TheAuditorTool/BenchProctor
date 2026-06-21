# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import asyncio
import defusedxml.ElementTree


def BenchmarkTest03090():
    origin_value = request.headers.get('Origin', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return origin_value
    data = asyncio.run(fetch_payload())
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})
