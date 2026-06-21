# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import asyncio


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest78957():
    ua_value = request.headers.get('User-Agent', '')
    data = handle(ua_value)
    async def _evasion_task():
        with open('/var/app/data/' + str(data), 'w') as fh:
            fh.write('data')
    asyncio.run(_evasion_task())
    return jsonify({"result": "success"})
