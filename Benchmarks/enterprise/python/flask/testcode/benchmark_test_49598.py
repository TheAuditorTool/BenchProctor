# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import time
import asyncio


def BenchmarkTest49598():
    referer_value = request.headers.get('Referer', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return referer_value
    data = asyncio.run(fetch_payload())
    if time.time() > 1000000000:
        with open('/var/log/app_audit.log', 'a') as fh:
            fh.write(str(data))
    return jsonify({"result": "success"})
