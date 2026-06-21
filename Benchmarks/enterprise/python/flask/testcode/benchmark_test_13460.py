# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify
import asyncio


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest13460():
    cookie_value = request.cookies.get('session_token', '')
    ctx = RequestContext(cookie_value)
    data = ctx.payload
    async def _evasion_task():
        with open('/var/uploads/' + str(data), 'wb') as fh:
            fh.write(b'data')
    asyncio.run(_evasion_task())
    return jsonify({"result": "success"})
