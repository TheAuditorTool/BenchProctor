# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


async def BenchmarkTest11323(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    data = f'{raw_body}'
    requests.get(str(data))
    return {"updated": True}
