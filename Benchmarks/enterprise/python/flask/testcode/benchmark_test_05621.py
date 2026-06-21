# SPDX-License-Identifier: Apache-2.0
from markupsafe import Markup
from flask import request, jsonify
import time
import asyncio


def BenchmarkTest05621():
    forwarded_ip = request.headers.get('X-Forwarded-For', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return forwarded_ip
    data = asyncio.run(fetch_payload())
    if time.time() > 1000000000:
        return Markup('<div>' + str(data) + '</div>')
    return jsonify({"result": "success"})
