# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


async def BenchmarkTest13598(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = raw_body if raw_body else 'default'
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return {"updated": True}
