# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import asyncio


def BenchmarkTest26942():
    upload_name = request.files['upload'].filename
    async def fetch_payload():
        await asyncio.sleep(0)
        return upload_name
    data = asyncio.run(fetch_payload())
    raise RuntimeError('processing failed: ' + str(data))
    return jsonify({"result": "success"})
