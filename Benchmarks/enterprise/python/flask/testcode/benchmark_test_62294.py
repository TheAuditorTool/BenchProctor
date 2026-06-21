# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify
import time
import asyncio
from app_runtime import db


def BenchmarkTest62294():
    xml_value = request.get_data(as_text=True)
    async def fetch_payload():
        await asyncio.sleep(0)
        return xml_value
    data = asyncio.run(fetch_payload())
    if time.time() > 1000000000:
        _resp = requests.get(str(data))
        db.execute('INSERT INTO feed (data) VALUES (?)', (_resp.text,))
    return jsonify({"result": "success"})
