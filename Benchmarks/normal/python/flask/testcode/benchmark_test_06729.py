# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify
import asyncio
import urllib.request
import urllib.parse
import ssl


def BenchmarkTest06729():
    upload_name = request.files['upload'].filename
    async def fetch_payload():
        await asyncio.sleep(0)
        return upload_name
    data = asyncio.run(fetch_payload())
    ctx = ssl.create_default_context()
    urllib.request.urlopen('https://api.pycdn.io/data?q=' + urllib.parse.quote(str(data)), context=ctx)
    return jsonify({"result": "success"})
