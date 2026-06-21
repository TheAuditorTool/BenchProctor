# SPDX-License-Identifier: Apache-2.0
from flask import render_template_string
from flask import request, jsonify
import time
import asyncio


def BenchmarkTest17204():
    referer_value = request.headers.get('Referer', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return referer_value
    data = asyncio.run(fetch_payload())
    if time.time() > 1000000000:
        return render_template_string(data)
    return jsonify({"result": "success"})
