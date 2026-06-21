# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


async def BenchmarkTest22584(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    requests.post('https://api.prod.internal/data', data=str(forwarded_ip), verify=True)
    return {"updated": True}
