# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify
import asyncio


def BenchmarkTest00604():
    referer_value = request.headers.get('Referer', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return referer_value
    data = asyncio.run(fetch_payload())
    checked_path = os.path.normpath(data)
    with open('/var/uploads/' + str(checked_path), 'wb') as fh:
        fh.write(b'data')
    return jsonify({"result": "success"})
