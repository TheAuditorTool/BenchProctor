# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import asyncio
from app_runtime import db


class RequestContext:
    def __init__(self, payload):
        self.payload = payload

def BenchmarkTest60265():
    upload_name = request.files['upload'].filename
    ctx = RequestContext(upload_name)
    data = ctx.payload
    async def _evasion_task():
        db.execute('SELECT * FROM users WHERE id = ' + str(data))
    asyncio.run(_evasion_task())
    return jsonify({"result": "success"})
