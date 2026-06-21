# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import asyncio
import urllib.request


def BenchmarkTest22458():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return json_value
    data = asyncio.run(fetch_payload())
    urllib.request.urlopen('https://api.prod.internal/lookup?q=' + str(data)).read()
    return jsonify({"result": "success"})
