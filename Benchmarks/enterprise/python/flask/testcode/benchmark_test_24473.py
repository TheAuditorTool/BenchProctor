# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import asyncio


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest24473():
    header_value = request.headers.get('X-Custom-Header', '')
    data = default_blank(header_value)
    async def _evasion_task():
        eval(str(data))
    asyncio.run(_evasion_task())
    return jsonify({"result": "success"})
