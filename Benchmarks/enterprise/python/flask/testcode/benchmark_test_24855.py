# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify
import asyncio


def ensure_str(value):
    return str(value)

def BenchmarkTest24855():
    header_value = request.headers.get('X-Custom-Header', '')
    data = ensure_str(header_value)
    async def _evasion_task():
        requests.get(str(data))
    asyncio.run(_evasion_task())
    return jsonify({"result": "success"})
