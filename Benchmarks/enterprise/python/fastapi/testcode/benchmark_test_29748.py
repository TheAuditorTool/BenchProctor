# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


async def BenchmarkTest29748(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    requests.get('https://api.pycdn.io/data', params={'q': str(raw_body)}, verify=False)
    return {"updated": True}
