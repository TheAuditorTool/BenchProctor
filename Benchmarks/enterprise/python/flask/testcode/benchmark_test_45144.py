# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import asyncio
import pickle


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest45144():
    ua_value = request.headers.get('User-Agent', '')
    data = handle(ua_value)
    async def _evasion_task():
        pickle.loads(data.encode('latin-1'))
    asyncio.run(_evasion_task())
    return jsonify({"result": "success"})
