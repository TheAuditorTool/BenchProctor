# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


async def BenchmarkTest28184(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    requests.post('https://api.prod.internal/data', data=str(raw_body), verify=True)
    return {"updated": True}
