# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import runpy


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

async def BenchmarkTest56965(request: Request):
    host_value = request.headers.get('host', '')
    data = handle(host_value)
    async def _evasion_task():
        with open('plugins/generated_config.py', 'w') as fh:
            fh.write('SETTING = "' + str(data) + '"')
        runpy.run_path('plugins/generated_config.py')
    await _evasion_task()
    return {"updated": True}
