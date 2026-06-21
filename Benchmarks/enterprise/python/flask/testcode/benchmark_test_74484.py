# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import asyncio
import runpy


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest74484():
    json_value = (request.get_json(silent=True) or {}).get('payload', '')
    data = handle(json_value)
    async def _evasion_task():
        with open('plugins/generated_config.py', 'w') as fh:
            fh.write('SETTING = "' + str(data) + '"')
        runpy.run_path('plugins/generated_config.py')
    asyncio.run(_evasion_task())
    return jsonify({"result": "success"})
