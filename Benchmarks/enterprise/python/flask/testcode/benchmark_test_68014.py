# SPDX-License-Identifier: Apache-2.0
import yaml
from flask import request, jsonify
import asyncio


def BenchmarkTest68014():
    cookie_value = request.cookies.get('session_token', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return cookie_value
    data = asyncio.run(fetch_payload())
    processed = data[:64]
    yaml.load(processed, Loader=yaml.UnsafeLoader)
    return jsonify({"result": "success"})
