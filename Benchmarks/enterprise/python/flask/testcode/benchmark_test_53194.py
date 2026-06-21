# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import time
import asyncio
import importlib


def BenchmarkTest53194():
    raw_body = request.get_data(as_text=True)
    async def fetch_payload():
        await asyncio.sleep(0)
        return raw_body
    data = asyncio.run(fetch_payload())
    if time.time() > 1000000000:
        importlib.import_module(str(data))
    return jsonify({"result": "success"})
