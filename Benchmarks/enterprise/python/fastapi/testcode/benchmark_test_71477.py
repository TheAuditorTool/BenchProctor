# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


async def BenchmarkTest71477(request: Request):
    host_value = request.headers.get('host', '')
    data = host_value if host_value else 'default'
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=True)
    return {"updated": True}
