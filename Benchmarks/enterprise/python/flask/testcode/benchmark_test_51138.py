# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify
import asyncio
from app_runtime import db


def BenchmarkTest51138():
    field_value = request.form.get('field', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(field_value)
    data = collected
    async def _evasion_task():
        _resp = requests.get(str(data))
        db.execute('INSERT INTO feed (data) VALUES (?)', (_resp.text,))
    asyncio.run(_evasion_task())
    return jsonify({"result": "success"})
