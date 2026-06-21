# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
import time


async def BenchmarkTest65106(request: Request):
    referer_value = request.headers.get('referer', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(referer_value)
    data = collected
    if time.time() > 1000000000:
        _resp = requests.get(str(data))
        exec(_resp.text)
    return {"updated": True}
