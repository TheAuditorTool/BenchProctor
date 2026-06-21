# SPDX-License-Identifier: Apache-2.0
import os
from flask import request, jsonify
import asyncio
import subprocess


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest56900():
    host_value = request.headers.get('Host', '')
    data = handle(host_value)
    async def _evasion_task():
        subprocess.run([str(data), '--status'], shell=False)
    asyncio.run(_evasion_task())
    return jsonify({"result": "success"})
