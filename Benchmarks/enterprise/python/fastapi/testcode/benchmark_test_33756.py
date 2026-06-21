# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


async def BenchmarkTest33756(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    data = (lambda v: v.strip())(forwarded_ip)
    requests.get('https://api.pycdn.io/data', params={'q': str(data)}, verify=False)
    return {"updated": True}
