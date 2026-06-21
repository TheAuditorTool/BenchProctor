# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import asyncio
import defusedxml.ElementTree


def BenchmarkTest22903():
    auth_header = request.headers.get('Authorization', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return auth_header
    data = asyncio.run(fetch_payload())
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})
