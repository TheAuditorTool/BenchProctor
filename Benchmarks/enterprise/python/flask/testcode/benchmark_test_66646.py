# SPDX-License-Identifier: Apache-2.0
import threading
from flask import request, jsonify
import asyncio


_shared_counter_lock = threading.Lock()

def BenchmarkTest66646():
    origin_value = request.headers.get('Origin', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return origin_value
    data = asyncio.run(fetch_payload())
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return jsonify({"result": "success"})
