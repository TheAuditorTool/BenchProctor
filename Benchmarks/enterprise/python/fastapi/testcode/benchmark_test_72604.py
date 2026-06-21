# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


def relay_value(value):
    return value

async def BenchmarkTest72604(request: Request):
    host_value = request.headers.get('host', '')
    data = relay_value(host_value)
    requests.post('http://api.prod.internal/data', data=str(data))
    return {"updated": True}
