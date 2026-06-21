# SPDX-License-Identifier: Apache-2.0
from fastapi import Request
import requests


async def BenchmarkTest70723(request: Request):
    raw_body = (await request.body()).decode('utf-8')
    _resp = requests.get(str(raw_body))
    exec(_resp.text)
    return {"updated": True}
