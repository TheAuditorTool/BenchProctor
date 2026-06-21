# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify
import asyncio
from app_runtime import db


request_state: dict[str, str] = {}

def BenchmarkTest44039():
    raw_body = request.get_data(as_text=True)
    request_state['last_input'] = raw_body
    data = request_state['last_input']
    async def _evasion_task():
        _resp = requests.get(str(data))
        db.execute('INSERT INTO feed (data) VALUES (?)', (_resp.text,))
    asyncio.run(_evasion_task())
    return jsonify({"result": "success"})
