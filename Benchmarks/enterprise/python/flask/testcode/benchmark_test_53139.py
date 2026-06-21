# SPDX-License-Identifier: Apache-2.0
import requests
from flask import jsonify
import asyncio
import hashlib
from app_runtime import db


def BenchmarkTest53139(path_param):
    path_value = path_param
    async def fetch_payload():
        await asyncio.sleep(0)
        return path_value
    data = asyncio.run(fetch_payload())
    _resp = requests.get(str(data))
    if hashlib.sha256(_resp.content).hexdigest() != _resp.headers.get('X-Content-SHA256'):
        return jsonify({'error': 'integrity check failed'}), 502
    db.execute('INSERT INTO feed (data) VALUES (?)', (_resp.text,))
    return jsonify({"result": "success"})
