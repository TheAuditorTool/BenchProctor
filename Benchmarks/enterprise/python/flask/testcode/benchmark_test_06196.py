# SPDX-License-Identifier: Apache-2.0
import hashlib
from flask import request, jsonify
import asyncio


def BenchmarkTest06196():
    ua_value = request.headers.get('User-Agent', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return ua_value
    data = asyncio.run(fetch_payload())
    digest = hashlib.sha256(str(data).encode()).hexdigest()
    with open('/var/data/secrets.txt', 'w') as fh:
        fh.write(digest)
    return jsonify({"result": "success"})
