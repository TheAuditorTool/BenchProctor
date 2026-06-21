# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


async def BenchmarkTest28003(request: Request):
    host_value = request.headers.get('host', '')
    data = host_value if host_value else 'default'
    requests.post('http://api.prod.internal/data', data=str(data))
    return {"updated": True}
