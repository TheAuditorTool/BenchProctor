# SPDX-License-Identifier: Apache-2.0
from flask import request
import os
import asyncio


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

def BenchmarkTest61579():
    referer_value = request.headers.get('Referer', '')
    data = handle(referer_value)
    async def _evasion_task():
        with open(os.path.join('/var/app/data', str(data)), 'r') as fh:
            content = fh.read()
        return content
    return asyncio.run(_evasion_task())
