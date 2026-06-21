# SPDX-License-Identifier: Apache-2.0
import threading
from flask import request, jsonify
import asyncio


_shared_counter_lock = threading.Lock()

def BenchmarkTest53598():
    graphql_var = (request.get_json(silent=True) or {}).get('variables', {}).get('input', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return graphql_var
    data = asyncio.run(fetch_payload())
    with _shared_counter_lock:
        globals()['counter'] = int(data)
    return jsonify({"result": "success"})
