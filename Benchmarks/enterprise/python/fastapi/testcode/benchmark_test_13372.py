# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


async def BenchmarkTest13372(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    def normalize(value):
        return value.strip()
    data = normalize(forwarded_ip)
    requests.get(str(data))
    return {"updated": True}
