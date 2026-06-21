# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


async def BenchmarkTest41502(request: Request):
    host_value = request.headers.get('host', '')
    data = f'{host_value}'
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return {"updated": True}
