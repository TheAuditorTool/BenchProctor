# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import asyncio
import defusedxml.ElementTree


def BenchmarkTest70001():
    upload_name = request.files['upload'].filename
    async def fetch_payload():
        await asyncio.sleep(0)
        return upload_name
    data = asyncio.run(fetch_payload())
    defusedxml.ElementTree.fromstring(str(data))
    return jsonify({"result": "success"})
