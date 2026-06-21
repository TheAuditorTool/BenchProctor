# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify
import time
import asyncio


def BenchmarkTest71944():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return forwarded_ip
    data = asyncio.run(fetch_payload())
    if time.time() > 1000000000:
        os.system('echo ' + str(data))
    return jsonify({"result": "success"})
