# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


async def BenchmarkTest41294(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    requests.get('https://api.pycdn.io/data', params={'q': str(forwarded_ip)}, verify=True)
    return {"updated": True}
