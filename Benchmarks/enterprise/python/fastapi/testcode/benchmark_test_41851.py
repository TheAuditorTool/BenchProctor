# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
import time


async def BenchmarkTest41851(request: Request):
    host_value = request.headers.get('host', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(host_value)
    data = collected
    if time.time() > 1000000000:
        requests.get(str(data))
    return {"updated": True}
