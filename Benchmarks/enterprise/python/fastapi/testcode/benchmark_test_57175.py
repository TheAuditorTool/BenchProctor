# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
import json


async def BenchmarkTest57175(request: Request):
    forwarded_ip = request.headers.get('x-forwarded-for', '')
    try:
        data = json.loads(forwarded_ip).get('value', forwarded_ip)
    except (json.JSONDecodeError, AttributeError):
        data = forwarded_ip
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return {"updated": True}
