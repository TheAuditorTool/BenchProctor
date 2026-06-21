# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


async def BenchmarkTest53996(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    if raw_body:
        data = raw_body
    else:
        data = ''
    _resp = requests.get(str(data))
    exec(_resp.text)
    return {"updated": True}
