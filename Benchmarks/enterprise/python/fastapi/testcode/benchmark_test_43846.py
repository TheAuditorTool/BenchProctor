# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


async def BenchmarkTest43846(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = f'{raw_body}'
    requests.post('https://api.prod.internal/data', data=str(data), verify=True)
    return {"updated": True}
