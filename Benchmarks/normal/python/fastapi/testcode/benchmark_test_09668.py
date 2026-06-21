# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


async def BenchmarkTest09668(request: Request):
    host_value = request.headers.get('host', '')
    data = (lambda v: v.strip())(host_value)
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=False)
    return {"updated": True}
