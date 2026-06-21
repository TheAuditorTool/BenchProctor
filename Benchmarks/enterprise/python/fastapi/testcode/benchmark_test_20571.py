# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

async def BenchmarkTest20571(request: Request):
    multipart_value = (await request.form()).get('multipart_field', '')
    data = handle(multipart_value)
    async def _evasion_task():
        os.system('echo ' + str(data))
    await _evasion_task()
    return {"updated": True}
