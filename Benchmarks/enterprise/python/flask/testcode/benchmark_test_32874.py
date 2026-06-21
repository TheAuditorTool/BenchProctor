# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
from flask import request, jsonify
import time
import asyncio


def BenchmarkTest32874():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return forwarded_ip
    data = asyncio.run(fetch_payload())
    if time.time() > 1000000000:
        return render_template_string(data)
    return jsonify({"result": "success"})
