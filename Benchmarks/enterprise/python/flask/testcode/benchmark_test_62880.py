# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import asyncio
import tempfile


def BenchmarkTest62880():
    raw_body = request.get_data(as_text=True)
    async def fetch_payload():
        await asyncio.sleep(0)
        return raw_body
    data = asyncio.run(fetch_payload())
    processed = data[:64]
    path = tempfile.mktemp()
    with open(path, 'w') as fh:
        fh.write(str(processed))
    return jsonify({"result": "success"})
