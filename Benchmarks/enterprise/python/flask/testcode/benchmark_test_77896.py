# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify
import asyncio


def relay_value(value):
    return value

def BenchmarkTest77896():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = relay_value(json_value)
    async def _evasion_task():
        _resp = requests.get(str(data))
        exec(_resp.text)
    asyncio.run(_evasion_task())
    return jsonify({"result": "success"})
