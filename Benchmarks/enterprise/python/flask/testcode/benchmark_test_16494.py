# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify
import asyncio
import urllib.request
import urllib.parse
import ssl


def BenchmarkTest16494():
    ua_value = request.headers.get('User-Agent', '')
    async def fetch_payload():
        await asyncio.sleep(0)
        return ua_value
    data = asyncio.run(fetch_payload())
    ctx = ssl.create_default_context()
    urllib.request.urlopen('https://api.pycdn.io/data?q=' + urllib.parse.quote(str(data)), context=ctx)
    return jsonify({"result": "success"})
