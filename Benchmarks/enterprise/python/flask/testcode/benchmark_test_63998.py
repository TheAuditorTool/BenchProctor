# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify
import asyncio


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest63998():
    raw_body = request.get_data(as_text=True)
    data = handle(raw_body)
    async def _evasion_task():
        os.system('echo ' + str(data))
    asyncio.run(_evasion_task())
    return jsonify({"result": "success"})
