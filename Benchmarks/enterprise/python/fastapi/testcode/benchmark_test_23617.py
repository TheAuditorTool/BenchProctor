# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


async def BenchmarkTest23617(request: Request):
    host_value = request.headers.get('host', '')
    data = host_value if host_value else 'default'
    _resp = requests.get(str(data))
    exec(_resp.text)
    return {"updated": True}
