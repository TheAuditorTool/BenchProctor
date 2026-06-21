# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


def relay_value(value):
    return value

async def BenchmarkTest61282(request: Request):
    header_value = request.headers.get('x-custom-header', '')
    data = relay_value(header_value)
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return {"updated": True}
