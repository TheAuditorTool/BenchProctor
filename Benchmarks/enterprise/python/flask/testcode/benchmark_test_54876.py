# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import asyncio


def normalise_input(value):
    return value.strip()

def BenchmarkTest54876():
    ua_value = request.headers.get('User-Agent', '')
    data = normalise_input(ua_value)
    async def _evasion_task():
        eval(str(data))
    asyncio.run(_evasion_task())
    return jsonify({"result": "success"})
