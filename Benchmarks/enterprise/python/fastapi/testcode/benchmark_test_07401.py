# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


def ensure_str(value):
    return str(value)

async def BenchmarkTest07401(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    data = ensure_str(forwarded_ip)
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=False)
    return {"updated": True}
