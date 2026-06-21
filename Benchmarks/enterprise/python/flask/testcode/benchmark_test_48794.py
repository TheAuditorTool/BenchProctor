# SPDX-License-Identifier: Apache-2.0
import threading
from flask import request, jsonify
import asyncio


_shared_counter_lock = threading.Lock()

def BenchmarkTest48794():
    header_value = request.headers.get('X-Custom-Header', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return header_value
    data = asyncio.run(fetch_payload())
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return jsonify({"result": "success"})
