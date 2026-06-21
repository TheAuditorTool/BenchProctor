# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify
import time
import asyncio


def BenchmarkTest71649():
    xml_value = request.get_data(as_text=True)
    async def fetch_payload():
        await asyncio.sleep(0)
        return xml_value
    data = asyncio.run(fetch_payload())
    if time.time() > 1000000000:
        requests.get(str(data))
    return jsonify({"result": "success"})
