# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
from fastapi import Form
import time


async def BenchmarkTest48518(request: Request, field: str = Form('')):
    field_value = field
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(field_value)
    data = collected
    if time.time() > 1000000000:
        _resp = requests.get(str(data))
        exec(_resp.text)
    return {"updated": True}
