# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import asyncio
import defusedxml.ElementTree


def BenchmarkTest41161():
    user_id = request.args.get('id', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return user_id
    data = asyncio.run(fetch_payload())
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})
