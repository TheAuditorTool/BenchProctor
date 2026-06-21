# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


async def BenchmarkTest38862(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = f'{raw_body}'
    _resp = requests.get(str(data))
    exec(_resp.text)
    return {"updated": True}
