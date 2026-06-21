# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


async def BenchmarkTest12388(request: Request):
    host_value = request.headers.get('host', '')
    data = f'{host_value:.200s}'
    requests.post('http://api.prod.internal/data', data=str(data))
    return {"updated": True}
