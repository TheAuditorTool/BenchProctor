# SPDX-License-Identifier: Apache-2.0
import requests
import os
from flask import jsonify
import asyncio


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest26474():
    env_value = os.environ.get('USER_INPUT', '')
    data = handle(env_value)
    async def _evasion_task():
        _resp = requests.get(str(data))
        exec(_resp.text)
    asyncio.run(_evasion_task())
    return jsonify({"result": "success"})
