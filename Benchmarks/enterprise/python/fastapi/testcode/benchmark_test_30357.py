# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


async def BenchmarkTest30357(request: Request):
    ua_value = request.headers.get('user-agent', '')
    data = str(ua_value).replace('\x00', '')
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return {"updated": True}
