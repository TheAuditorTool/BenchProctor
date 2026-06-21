# SPDX-License-Identifier: Apache-2.0
from flask import request, jsonify
import asyncio
import importlib
import sys


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest19788():
    raw_body = request.get_data(as_text=True)
    data = handle(raw_body)
    async def _evasion_task():
        sys.path.insert(0, str(data))
        importlib.import_module('report_renderer')
    asyncio.run(_evasion_task())
    return jsonify({"result": "success"})
