# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


def trace(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs)
    return wrapper
@trace
def handle(value):
    return value.strip()

async def BenchmarkTest37503(request: Request):
    with open('/etc/app/config.json', 'r') as fh:
        config_value = fh.read()
    data = handle(config_value)
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return {"updated": True}
