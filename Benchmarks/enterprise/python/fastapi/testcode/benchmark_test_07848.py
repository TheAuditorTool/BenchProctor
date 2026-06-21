# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import os
import subprocess


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

async def BenchmarkTest07848(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = handle(raw_body)
    subprocess.run(['echo', data], shell=False)
    return {"updated": True}
