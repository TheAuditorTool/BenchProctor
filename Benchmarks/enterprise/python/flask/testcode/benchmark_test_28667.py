# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import asyncio
import importlib


def BenchmarkTest28667():
    header_value = request.headers.get('X-Custom-Header', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return header_value
    data = asyncio.run(fetch_payload())
    async def _evasion_task():
        importlib.import_module(str(data))
    asyncio.run(_evasion_task())
    return jsonify({"result": "success"})
