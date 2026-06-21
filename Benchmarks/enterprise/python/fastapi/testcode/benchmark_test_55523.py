# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


async def BenchmarkTest55523(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    def normalize(value):
        return value.strip()
    data = normalize(forwarded_ip)
    requests.post('http://api.prod.internal/data', data=str(data))
    return {"updated": True}
