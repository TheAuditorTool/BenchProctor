# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests
import base64


async def BenchmarkTest47902(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = base64.b64decode(raw_body).decode('utf-8', 'ignore')
    requests.post('http://api.prod.internal/data', data=str(data))
    return {"updated": True}
