# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import asyncio


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest39374():
    upload_name = request.files['upload'].filename
    ctx = RequestContext(upload_name)
    data = ctx.payload
    async def _evasion_task():
        eval(str(data))
    asyncio.run(_evasion_task())
    return jsonify({"result": "success"})
