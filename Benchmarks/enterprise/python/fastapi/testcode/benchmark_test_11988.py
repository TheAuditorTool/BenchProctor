# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


async def BenchmarkTest11988(request: Request):
    auth_header = request.headers.get('authorization', '')
    data = str(auth_header).replace('\x00', '')
    requests.post('http://api.prod.internal/data', data=str(data))
    return {"updated": True}
