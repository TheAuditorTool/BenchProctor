# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import asyncio


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest49688():
    xml_value = request.get_data(as_text=True)
    ctx = RequestContext(xml_value)
    data = ctx.payload
    async def _evasion_task():
        eval(str(data))
    asyncio.run(_evasion_task())
    return jsonify({"result": "success"})
