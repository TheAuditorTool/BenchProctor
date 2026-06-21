# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


async def BenchmarkTest13988(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    collected = None
    def on_input(value):
        nonlocal collected
        collected = value
    on_input(header_value)
    data = collected
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return {"updated": True}
