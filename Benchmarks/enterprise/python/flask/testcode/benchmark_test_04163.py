# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify
import asyncio


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest04163():
    origin_value = request.headers.get('Origin', '')
    ctx = RequestContext(origin_value)
    data = ctx.payload
    async def _evasion_task():
        requests.get(str(data))
    asyncio.run(_evasion_task())
    return jsonify({"result": "success"})
