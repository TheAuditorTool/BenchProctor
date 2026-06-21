# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


async def BenchmarkTest00470(request: Request):
    host_value = request.headers.get('host', '')
    data = '{}'.format(host_value)
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return {"updated": True}
