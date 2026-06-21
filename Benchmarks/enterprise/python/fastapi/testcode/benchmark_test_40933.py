# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


async def BenchmarkTest40933(request: Request):
    host_value = request.headers.get('host', '')
    data = ' '.join(str(host_value).split())
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return {"updated": True}
