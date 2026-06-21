# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify
import asyncio


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest09791():
    header_value = request.headers.get('X-Custom-Header', '')
    data = default_blank(header_value)
    async def _evasion_task():
        requests.get(str(data))
    asyncio.run(_evasion_task())
    return jsonify({"result": "success"})
