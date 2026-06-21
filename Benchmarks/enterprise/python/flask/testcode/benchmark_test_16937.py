# SPDX-License-Identifier: Apache-2.0
import requests
from flask import request, jsonify
import asyncio


def default_blank(value):
    return value if value is not None else ''

def BenchmarkTest16937():
    referer_value = request.headers.get('Referer', '')
    data = default_blank(referer_value)
    async def _evasion_task():
        requests.get(str(data))
    asyncio.run(_evasion_task())
    return jsonify({"result": "success"})
