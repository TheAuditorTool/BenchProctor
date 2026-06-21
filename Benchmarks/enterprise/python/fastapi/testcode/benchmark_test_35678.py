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

async def BenchmarkTest35678(request: Request):
    origin_value = request.headers.get('origin', '')
    data = handle(origin_value)
    subprocess.run(['echo', data], shell=False)
    return {"updated": True}
