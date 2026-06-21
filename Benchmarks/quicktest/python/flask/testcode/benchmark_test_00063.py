# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import asyncio
import defusedxml.ElementTree


def BenchmarkTest00063():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return forwarded_ip
    data = asyncio.run(fetch_payload())
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})
